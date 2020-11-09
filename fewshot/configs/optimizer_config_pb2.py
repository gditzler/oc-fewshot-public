# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fewshot/configs/optimizer_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fewshot/configs/optimizer_config.proto',
  package='fewshot.configs',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n&fewshot/configs/optimizer_config.proto\x12\x0f\x66\x65wshot.configs\"\xe1\x01\n\x0fOptimizerConfig\x12\x11\n\toptimizer\x18\x01 \x01(\t\x12\x0f\n\x07lr_list\x18\x02 \x03(\x02\x12\x16\n\x0elr_decay_steps\x18\x03 \x03(\x05\x12\x17\n\x0fmax_train_steps\x18\x04 \x01(\x05\x12\x12\n\nbatch_size\x18\x05 \x01(\x05\x12\x12\n\x07num_gpu\x18\x06 \x01(\x05:\x01\x31\x12\x14\n\tclip_norm\x18\x07 \x01(\x02:\x01\x30\x12!\n\x19inner_loop_truncate_steps\x18\x08 \x01(\x05\x12\x18\n\nlr_scaling\x18\t \x01(\x08:\x04true')
)




_OPTIMIZERCONFIG = _descriptor.Descriptor(
  name='OptimizerConfig',
  full_name='fewshot.configs.OptimizerConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='fewshot.configs.OptimizerConfig.optimizer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lr_list', full_name='fewshot.configs.OptimizerConfig.lr_list', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lr_decay_steps', full_name='fewshot.configs.OptimizerConfig.lr_decay_steps', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_train_steps', full_name='fewshot.configs.OptimizerConfig.max_train_steps', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='fewshot.configs.OptimizerConfig.batch_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_gpu', full_name='fewshot.configs.OptimizerConfig.num_gpu', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clip_norm', full_name='fewshot.configs.OptimizerConfig.clip_norm', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inner_loop_truncate_steps', full_name='fewshot.configs.OptimizerConfig.inner_loop_truncate_steps', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lr_scaling', full_name='fewshot.configs.OptimizerConfig.lr_scaling', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=285,
)

DESCRIPTOR.message_types_by_name['OptimizerConfig'] = _OPTIMIZERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OptimizerConfig = _reflection.GeneratedProtocolMessageType('OptimizerConfig', (_message.Message,), dict(
  DESCRIPTOR = _OPTIMIZERCONFIG,
  __module__ = 'fewshot.configs.optimizer_config_pb2'
  # @@protoc_insertion_point(class_scope:fewshot.configs.OptimizerConfig)
  ))
_sym_db.RegisterMessage(OptimizerConfig)


# @@protoc_insertion_point(module_scope)
