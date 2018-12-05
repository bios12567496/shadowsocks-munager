# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/common/net/network.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/common/net/network.proto',
  package='v2ray.core.common.net',
  syntax='proto3',
  serialized_options=_b('\n\031com.v2ray.core.common.netP\001Z\003net\252\002\025V2Ray.Core.Common.Net'),
  serialized_pb=_b('\n\'v2ray.com/core/common/net/network.proto\x12\x15v2ray.core.common.net\">\n\x0bNetworkList\x12/\n\x07network\x18\x01 \x03(\x0e\x32\x1e.v2ray.core.common.net.Network*8\n\x07Network\x12\x0b\n\x07Unknown\x10\x00\x12\x0e\n\x06RawTCP\x10\x01\x1a\x02\x08\x01\x12\x07\n\x03TCP\x10\x02\x12\x07\n\x03UDP\x10\x03\x42:\n\x19\x63om.v2ray.core.common.netP\x01Z\x03net\xaa\x02\x15V2Ray.Core.Common.Netb\x06proto3')
)

_NETWORK = _descriptor.EnumDescriptor(
  name='Network',
  full_name='v2ray.core.common.net.Network',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RawTCP', index=1, number=1,
      serialized_options=_b('\010\001'),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TCP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UDP', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=130,
  serialized_end=186,
)
_sym_db.RegisterEnumDescriptor(_NETWORK)

Network = enum_type_wrapper.EnumTypeWrapper(_NETWORK)
Unknown = 0
RawTCP = 1
TCP = 2
UDP = 3



_NETWORKLIST = _descriptor.Descriptor(
  name='NetworkList',
  full_name='v2ray.core.common.net.NetworkList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network', full_name='v2ray.core.common.net.NetworkList.network', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=128,
)

_NETWORKLIST.fields_by_name['network'].enum_type = _NETWORK
DESCRIPTOR.message_types_by_name['NetworkList'] = _NETWORKLIST
DESCRIPTOR.enum_types_by_name['Network'] = _NETWORK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NetworkList = _reflection.GeneratedProtocolMessageType('NetworkList', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKLIST,
  __module__ = 'v2ray.com.core.common.net.network_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.common.net.NetworkList)
  ))
_sym_db.RegisterMessage(NetworkList)


DESCRIPTOR._options = None
_NETWORK.values_by_name["RawTCP"]._options = None
# @@protoc_insertion_point(module_scope)