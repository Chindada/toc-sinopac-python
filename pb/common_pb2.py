# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63ommon.proto\x12\x11sinopac_forwarder\"f\n\x0c\x45ventMessage\x12\x11\n\tresp_code\x18\x01 \x01(\x03\x12\x12\n\nevent_code\x18\x02 \x01(\x03\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\r\n\x05\x65vent\x18\x04 \x01(\t\x12\x12\n\nevent_time\x18\x05 \x01(\t\"\xae\x03\n\x18StockRealTimeTickMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x11\n\tavg_price\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x0c\n\x04high\x18\x06 \x01(\x01\x12\x0b\n\x03low\x18\x07 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x08 \x01(\x01\x12\x14\n\x0ctotal_amount\x18\t \x01(\x01\x12\x0e\n\x06volume\x18\n \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0b \x01(\x03\x12\x11\n\ttick_type\x18\x0c \x01(\x03\x12\x10\n\x08\x63hg_type\x18\r \x01(\x03\x12\x11\n\tprice_chg\x18\x0e \x01(\x01\x12\x0f\n\x07pct_chg\x18\x0f \x01(\x01\x12\x1a\n\x12\x62id_side_total_vol\x18\x10 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_vol\x18\x11 \x01(\x03\x12\x1a\n\x12\x62id_side_total_cnt\x18\x12 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_cnt\x18\x13 \x01(\x03\x12\x0f\n\x07suspend\x18\x14 \x01(\x03\x12\x10\n\x08simtrade\x18\x15 \x01(\x03\"\x80\x03\n\x19\x46utureRealTimeTickMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x18\n\x10underlying_price\x18\x04 \x01(\x01\x12\x1a\n\x12\x62id_side_total_vol\x18\x05 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_vol\x18\x06 \x01(\x03\x12\x11\n\tavg_price\x18\x07 \x01(\x01\x12\r\n\x05\x63lose\x18\x08 \x01(\x01\x12\x0c\n\x04high\x18\t \x01(\x01\x12\x0b\n\x03low\x18\n \x01(\x01\x12\x0e\n\x06\x61mount\x18\x0b \x01(\x01\x12\x14\n\x0ctotal_amount\x18\x0c \x01(\x01\x12\x0e\n\x06volume\x18\r \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0e \x01(\x03\x12\x11\n\ttick_type\x18\x0f \x01(\x03\x12\x10\n\x08\x63hg_type\x18\x10 \x01(\x03\x12\x11\n\tprice_chg\x18\x11 \x01(\x01\x12\x0f\n\x07pct_chg\x18\x12 \x01(\x01\x12\x10\n\x08simtrade\x18\x13 \x01(\x03\"\xda\x01\n\x1aStockRealTimeBidAskMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x11\n\tbid_price\x18\x03 \x03(\x01\x12\x12\n\nbid_volume\x18\x04 \x03(\x03\x12\x14\n\x0c\x64iff_bid_vol\x18\x05 \x03(\x03\x12\x11\n\task_price\x18\x06 \x03(\x01\x12\x12\n\nask_volume\x18\x07 \x03(\x03\x12\x14\n\x0c\x64iff_ask_vol\x18\x08 \x03(\x03\x12\x0f\n\x07suspend\x18\t \x01(\x03\x12\x10\n\x08simtrade\x18\n \x01(\x03\"\x1b\n\x0c\x45rrorMessage\x12\x0b\n\x03\x65rr\x18\x01 \x01(\t\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"$\n\x0bStockNumArr\x12\x15\n\rstock_num_arr\x18\x01 \x03(\t\":\n\x13StockNumArrWithDate\x12\x15\n\rstock_num_arr\x18\x01 \x03(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\"A\n\x16StockNumArrWithDateArr\x12\x15\n\rstock_num_arr\x18\x01 \x03(\t\x12\x10\n\x08\x64\x61te_arr\x18\x02 \x03(\t\"(\n\rFutureCodeArr\x12\x17\n\x0f\x66uture_code_arr\x18\x01 \x03(\t\">\n\x15\x46utureCodeArrWithDate\x12\x17\n\x0f\x66uture_code_arr\x18\x01 \x03(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\tB\x06Z\x04./pbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\004./pb'
  _EVENTMESSAGE._serialized_start=35
  _EVENTMESSAGE._serialized_end=137
  _STOCKREALTIMETICKMESSAGE._serialized_start=140
  _STOCKREALTIMETICKMESSAGE._serialized_end=570
  _FUTUREREALTIMETICKMESSAGE._serialized_start=573
  _FUTUREREALTIMETICKMESSAGE._serialized_end=957
  _STOCKREALTIMEBIDASKMESSAGE._serialized_start=960
  _STOCKREALTIMEBIDASKMESSAGE._serialized_end=1178
  _ERRORMESSAGE._serialized_start=1180
  _ERRORMESSAGE._serialized_end=1207
  _DATE._serialized_start=1209
  _DATE._serialized_end=1229
  _STOCKNUMARR._serialized_start=1231
  _STOCKNUMARR._serialized_end=1267
  _STOCKNUMARRWITHDATE._serialized_start=1269
  _STOCKNUMARRWITHDATE._serialized_end=1327
  _STOCKNUMARRWITHDATEARR._serialized_start=1329
  _STOCKNUMARRWITHDATEARR._serialized_end=1394
  _FUTURECODEARR._serialized_start=1396
  _FUTURECODEARR._serialized_end=1436
  _FUTURECODEARRWITHDATE._serialized_start=1438
  _FUTURECODEARRWITHDATE._serialized_end=1500
# @@protoc_insertion_point(module_scope)
