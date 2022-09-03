# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: history.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rhistory.proto\x12\x11sinopac_forwarder\x1a\x0c\x63ommon.proto\"J\n\x13HistoryTickResponse\x12\x33\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32%.sinopac_forwarder.HistoryTickMessage\"\xae\x01\n\x12HistoryTickMessage\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\r\n\x05\x63lose\x18\x02 \x01(\x01\x12\x0e\n\x06volume\x18\x03 \x01(\x03\x12\x11\n\tbid_price\x18\x04 \x01(\x01\x12\x12\n\nbid_volume\x18\x05 \x01(\x03\x12\x11\n\task_price\x18\x06 \x01(\x01\x12\x12\n\nask_volume\x18\x07 \x01(\x03\x12\x11\n\ttick_type\x18\x08 \x01(\x03\x12\x0c\n\x04\x63ode\x18\t \x01(\t\"J\n\x13HistoryKbarResponse\x12\x33\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32%.sinopac_forwarder.HistoryKbarMessage\"v\n\x12HistoryKbarMessage\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\r\n\x05\x63lose\x18\x02 \x01(\x01\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x0c\n\x04high\x18\x04 \x01(\x01\x12\x0b\n\x03low\x18\x05 \x01(\x01\x12\x0e\n\x06volume\x18\x06 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x07 \x01(\t\"L\n\x14HistoryCloseResponse\x12\x34\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32&.sinopac_forwarder.HistoryCloseMessage\"@\n\x13HistoryCloseMessage\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\r\n\x05\x63lose\x18\x03 \x01(\x01\x32\xa9\x08\n\x14HistoryDataInterface\x12g\n\x13GetStockHistoryTick\x12&.sinopac_forwarder.StockNumArrWithDate\x1a&.sinopac_forwarder.HistoryTickResponse\"\x00\x12g\n\x13GetStockHistoryKbar\x12&.sinopac_forwarder.StockNumArrWithDate\x1a&.sinopac_forwarder.HistoryKbarResponse\"\x00\x12i\n\x14GetStockHistoryClose\x12&.sinopac_forwarder.StockNumArrWithDate\x1a\'.sinopac_forwarder.HistoryCloseResponse\"\x00\x12u\n\x1dGetStockHistoryCloseByDateArr\x12).sinopac_forwarder.StockNumArrWithDateArr\x1a\'.sinopac_forwarder.HistoryCloseResponse\"\x00\x12[\n\x16GetStockTSEHistoryTick\x12\x17.sinopac_forwarder.Date\x1a&.sinopac_forwarder.HistoryTickResponse\"\x00\x12[\n\x16GetStockTSEHistoryKbar\x12\x17.sinopac_forwarder.Date\x1a&.sinopac_forwarder.HistoryKbarResponse\"\x00\x12]\n\x17GetStockTSEHistoryClose\x12\x17.sinopac_forwarder.Date\x1a\'.sinopac_forwarder.HistoryCloseResponse\"\x00\x12j\n\x14GetFutureHistoryTick\x12(.sinopac_forwarder.FutureCodeArrWithDate\x1a&.sinopac_forwarder.HistoryTickResponse\"\x00\x12l\n\x15GetFutureHistoryClose\x12(.sinopac_forwarder.FutureCodeArrWithDate\x1a\'.sinopac_forwarder.HistoryCloseResponse\"\x00\x12j\n\x14GetFutureHistoryKbar\x12(.sinopac_forwarder.FutureCodeArrWithDate\x1a&.sinopac_forwarder.HistoryKbarResponse\"\x00\x42\x06Z\x04./pbb\x06proto3')



_HISTORYTICKRESPONSE = DESCRIPTOR.message_types_by_name['HistoryTickResponse']
_HISTORYTICKMESSAGE = DESCRIPTOR.message_types_by_name['HistoryTickMessage']
_HISTORYKBARRESPONSE = DESCRIPTOR.message_types_by_name['HistoryKbarResponse']
_HISTORYKBARMESSAGE = DESCRIPTOR.message_types_by_name['HistoryKbarMessage']
_HISTORYCLOSERESPONSE = DESCRIPTOR.message_types_by_name['HistoryCloseResponse']
_HISTORYCLOSEMESSAGE = DESCRIPTOR.message_types_by_name['HistoryCloseMessage']
HistoryTickResponse = _reflection.GeneratedProtocolMessageType('HistoryTickResponse', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYTICKRESPONSE,
  '__module__' : 'history_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.HistoryTickResponse)
  })
_sym_db.RegisterMessage(HistoryTickResponse)

HistoryTickMessage = _reflection.GeneratedProtocolMessageType('HistoryTickMessage', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYTICKMESSAGE,
  '__module__' : 'history_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.HistoryTickMessage)
  })
_sym_db.RegisterMessage(HistoryTickMessage)

HistoryKbarResponse = _reflection.GeneratedProtocolMessageType('HistoryKbarResponse', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYKBARRESPONSE,
  '__module__' : 'history_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.HistoryKbarResponse)
  })
_sym_db.RegisterMessage(HistoryKbarResponse)

HistoryKbarMessage = _reflection.GeneratedProtocolMessageType('HistoryKbarMessage', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYKBARMESSAGE,
  '__module__' : 'history_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.HistoryKbarMessage)
  })
_sym_db.RegisterMessage(HistoryKbarMessage)

HistoryCloseResponse = _reflection.GeneratedProtocolMessageType('HistoryCloseResponse', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYCLOSERESPONSE,
  '__module__' : 'history_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.HistoryCloseResponse)
  })
_sym_db.RegisterMessage(HistoryCloseResponse)

HistoryCloseMessage = _reflection.GeneratedProtocolMessageType('HistoryCloseMessage', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYCLOSEMESSAGE,
  '__module__' : 'history_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.HistoryCloseMessage)
  })
_sym_db.RegisterMessage(HistoryCloseMessage)

_HISTORYDATAINTERFACE = DESCRIPTOR.services_by_name['HistoryDataInterface']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\004./pb'
  _HISTORYTICKRESPONSE._serialized_start=50
  _HISTORYTICKRESPONSE._serialized_end=124
  _HISTORYTICKMESSAGE._serialized_start=127
  _HISTORYTICKMESSAGE._serialized_end=301
  _HISTORYKBARRESPONSE._serialized_start=303
  _HISTORYKBARRESPONSE._serialized_end=377
  _HISTORYKBARMESSAGE._serialized_start=379
  _HISTORYKBARMESSAGE._serialized_end=497
  _HISTORYCLOSERESPONSE._serialized_start=499
  _HISTORYCLOSERESPONSE._serialized_end=575
  _HISTORYCLOSEMESSAGE._serialized_start=577
  _HISTORYCLOSEMESSAGE._serialized_end=641
  _HISTORYDATAINTERFACE._serialized_start=644
  _HISTORYDATAINTERFACE._serialized_end=1709
# @@protoc_insertion_point(module_scope)
