# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: upload.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cupload.proto\":\n\rUploadRequest\x12\x14\n\x0c\x61pkfile_name\x18\x01 \x01(\t\x12\x13\n\x0b\x61pk_content\x18\x02 \x01(\x0c\"!\n\x0eUploadResponse\x12\x0f\n\x07message\x18\x01 \x01(\t28\n\x0bYourService\x12)\n\x06Upload\x12\x0e.UploadRequest\x1a\x0f.UploadResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'upload_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_UPLOADREQUEST']._serialized_start=16
  _globals['_UPLOADREQUEST']._serialized_end=74
  _globals['_UPLOADRESPONSE']._serialized_start=76
  _globals['_UPLOADRESPONSE']._serialized_end=109
  _globals['_YOURSERVICE']._serialized_start=111
  _globals['_YOURSERVICE']._serialized_end=167
# @@protoc_insertion_point(module_scope)
