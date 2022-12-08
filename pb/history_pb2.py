# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: history.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rhistory.proto\x12\x11sinopac_forwarder\x1a\x0c\x63ommon.proto\"J\n\x13HistoryTickResponse\x12\x33\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32%.sinopac_forwarder.HistoryTickMessage\"\xae\x01\n\x12HistoryTickMessage\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\r\n\x05\x63lose\x18\x02 \x01(\x01\x12\x0e\n\x06volume\x18\x03 \x01(\x03\x12\x11\n\tbid_price\x18\x04 \x01(\x01\x12\x12\n\nbid_volume\x18\x05 \x01(\x03\x12\x11\n\task_price\x18\x06 \x01(\x01\x12\x12\n\nask_volume\x18\x07 \x01(\x03\x12\x11\n\ttick_type\x18\x08 \x01(\x03\x12\x0c\n\x04\x63ode\x18\t \x01(\t\"J\n\x13HistoryKbarResponse\x12\x33\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32%.sinopac_forwarder.HistoryKbarMessage\"v\n\x12HistoryKbarMessage\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\r\n\x05\x63lose\x18\x02 \x01(\x01\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x0c\n\x04high\x18\x04 \x01(\x01\x12\x0b\n\x03low\x18\x05 \x01(\x01\x12\x0e\n\x06volume\x18\x06 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x07 \x01(\t\"L\n\x14HistoryCloseResponse\x12\x34\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32&.sinopac_forwarder.HistoryCloseMessage\"@\n\x13HistoryCloseMessage\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\r\n\x05\x63lose\x18\x03 \x01(\x01\x32\x81\t\n\x14HistoryDataInterface\x12g\n\x13GetStockHistoryTick\x12&.sinopac_forwarder.StockNumArrWithDate\x1a&.sinopac_forwarder.HistoryTickResponse\"\x00\x12g\n\x13GetStockHistoryKbar\x12&.sinopac_forwarder.StockNumArrWithDate\x1a&.sinopac_forwarder.HistoryKbarResponse\"\x00\x12i\n\x14GetStockHistoryClose\x12&.sinopac_forwarder.StockNumArrWithDate\x1a\'.sinopac_forwarder.HistoryCloseResponse\"\x00\x12u\n\x1dGetStockHistoryCloseByDateArr\x12).sinopac_forwarder.StockNumArrWithDateArr\x1a\'.sinopac_forwarder.HistoryCloseResponse\"\x00\x12[\n\x16GetStockTSEHistoryTick\x12\x17.sinopac_forwarder.Date\x1a&.sinopac_forwarder.HistoryTickResponse\"\x00\x12[\n\x16GetStockTSEHistoryKbar\x12\x17.sinopac_forwarder.Date\x1a&.sinopac_forwarder.HistoryKbarResponse\"\x00\x12]\n\x17GetStockTSEHistoryClose\x12\x17.sinopac_forwarder.Date\x1a\'.sinopac_forwarder.HistoryCloseResponse\"\x00\x12V\n\x11GetOTCHistoryKbar\x12\x17.sinopac_forwarder.Date\x1a&.sinopac_forwarder.HistoryKbarResponse\"\x00\x12j\n\x14GetFutureHistoryTick\x12(.sinopac_forwarder.FutureCodeArrWithDate\x1a&.sinopac_forwarder.HistoryTickResponse\"\x00\x12l\n\x15GetFutureHistoryClose\x12(.sinopac_forwarder.FutureCodeArrWithDate\x1a\'.sinopac_forwarder.HistoryCloseResponse\"\x00\x12j\n\x14GetFutureHistoryKbar\x12(.sinopac_forwarder.FutureCodeArrWithDate\x1a&.sinopac_forwarder.HistoryKbarResponse\"\x00\x42\x06Z\x04./pbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'history_pb2', globals())
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
  _HISTORYDATAINTERFACE._serialized_end=1797
# @@protoc_insertion_point(module_scope)
