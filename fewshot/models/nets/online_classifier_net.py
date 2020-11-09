"""Online classifier network.
This will run a classifier among the examples up till the current one. It is
similar to an example-based storage.

Author: Mengye Ren (mren@cs.toronto.edu)
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import tensorflow as tf

from fewshot.models.nets.episode_recurrent_sigmoid_net import EpisodeRecurrentSigmoidNet  # NOQA
from fewshot.models.nets.episode_recurrent_sigmoid_net import dummy_context_mgr
from fewshot.models.registry import RegisterModel


@RegisterModel("online_classifier_net")  # Legacy name
class OnlineClassifierNet(EpisodeRecurrentSigmoidNet):

  def __init__(self,
               config,
               backbone,
               memory,
               distributed=False,
               dtype=tf.float32):
    super(OnlineClassifierNet, self).__init__(
        config, backbone, distributed=distributed, dtype=dtype)
    self._memory = memory

  def forward(self, x, y, x_test=None, is_training=tf.constant(True),
              **kwargs):
    """Make a forward pass.

    Args:
      x: [B, T, ...]. Support examples at each timestep.
      y: [B, T]. Support labels at each timestep, note that the label is not
        revealed until the next step.

    Returns:
      y_pred: [B, T, K+1], Logits at each timestep.
    """
    T = tf.constant(x.shape[1])
    h = self.run_backbone(x, is_training=is_training)
    y_pred = tf.TensorArray(self.dtype, size=T)
    states = self.memory.get_initial_state(h.shape[0])

    for t in tf.range(T):
      x_ = self.slice_time(h, t)  # [B, ...]
      y_ = self.slice_time(y, t)  # [B]
      y_pred_, states = self.memory.forward_one(
          x_, y_, t, *states, is_training=is_training)
      # print(t, y_pred_, y_)
      y_pred = y_pred.write(t, y_pred_)
    y_pred = tf.transpose(y_pred.stack(), [1, 0, 2])
    if x_test is not None:
      assert False
    return y_pred

  @property
  def memory(self):
    """Memory module."""
    return self._memory

  def train_step(self,
                 x,
                 y,
                 s=None,
                 y_gt=None,
                 flag=None,
                 x_test=None,
                 y_test=None,
                 flag_test=None,
                 writer=None,
                 **kwargs):
    """One training step.

    Args:
      x: [B, T, ...], inputs at each timestep.
      y: [B, T], label at each timestep, to be fed as input.
      y_unk: [B, T], binary label indicating unknown, used as groundtruth.
      y_gt: [B, T], groundtruth at each timestep, if different from labels.
      x_test: [B, M, ...], inputs of the query set, optional.
      y_test: [B, M], groundtruth of the query set, optional.

    Returns:
      xent: Cross entropy loss.
    """
    if self._distributed:
      import horovod.tensorflow as hvd
    if y_gt is None:
      y_gt = y
    with writer.as_default() if writer is not None else dummy_context_mgr(
    ) as gs:
      with tf.GradientTape() as tape:
        loss, metric = self.compute_loss(
            x,
            y,
            y_gt,
            s=s,
            flag=flag,
            x_test=x_test,
            y_test=y_test,
            flag_test=flag_test,
            **kwargs)

      # Data parallel training.
      if self._distributed:
        xent_sync = tf.reduce_mean(
            hvd.allgather(
                tf.zeros([1], dtype=tf.float32) + metric['xent'], name='xent'))
        tape = hvd.DistributedGradientTape(tape)
      else:
        xent_sync = metric['xent']

      # Apply gradients.
      self.apply_gradients(loss, tape)

      write_flag = self._distributed and hvd.rank() == 0
      write_flag = write_flag or (not self._distributed)

      if write_flag and writer is not None:
        if tf.equal(
            tf.math.floormod(self._step + 1,
                             self.config.train_config.steps_per_log), 0):
          for name, val in metric.items():
            if name != 'xent':
              tf.summary.scalar(name, val, step=self._step + 1)
          writer.flush()
    return xent_sync

  def eval_step(self, x, y, **kwargs):
    """One evaluation step.
    Args:
      x: [B, T, ...], inputs at each timestep.
      y: [B, T], label at each timestep.
      x_test: [B, M, ...], inputs of the query set, optional.

    Returns:
      logits: [B, T, Kmax], prediction.
      logits_test: [B, M, Kmax], prediction on the query set, optional.
    """
    # Note that the model itself is still a cascaded output model. It doesn't
    # mean that we renormalize the logits. But for evaluating accuracy purpose
    # renormalizing the logits makes sure that we stay the same as our original
    # evaluation methods.
    logits = self.forward(x, y, is_training=tf.constant(False))
    return logits
