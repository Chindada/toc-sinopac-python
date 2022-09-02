# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/trade.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from pb import common_pb2 as pb_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epb/trade.proto\x12\x11sinopac_forwarder\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0fpb/common.proto\"X\n\x10StockOrderDetail\x12\x11\n\tstock_num\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12\x10\n\x08simulate\x18\x04 \x01(\x08\"B\n\x11\x46utureOrderDetail\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x10\n\x08quantity\x18\x03 \x01(\x03\">\n\x0bTradeResult\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"-\n\x07OrderID\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x10\n\x08simulate\x18\x02 \x01(\x08\"!\n\rFutureOrderID\x12\x10\n\x08order_id\x18\x01 \x01(\t\"H\n\x13StockOrderStatusArr\x12\x31\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32#.sinopac_forwarder.StockOrderStatus\"\x87\x01\n\x10StockOrderStatus\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x01\x12\x10\n\x08quantity\x18\x05 \x01(\x03\x12\x10\n\x08order_id\x18\x06 \x01(\t\x12\x12\n\norder_time\x18\x07 \x01(\t2\xba\x07\n\x0eTradeInterface\x12Q\n\x08\x42uyStock\x12#.sinopac_forwarder.StockOrderDetail\x1a\x1e.sinopac_forwarder.TradeResult\"\x00\x12R\n\tSellStock\x12#.sinopac_forwarder.StockOrderDetail\x1a\x1e.sinopac_forwarder.TradeResult\"\x00\x12W\n\x0eSellFirstStock\x12#.sinopac_forwarder.StockOrderDetail\x1a\x1e.sinopac_forwarder.TradeResult\"\x00\x12K\n\x0b\x43\x61ncelStock\x12\x1a.sinopac_forwarder.OrderID\x1a\x1e.sinopac_forwarder.TradeResult\"\x00\x12R\n\x12GetOrderStatusByID\x12\x1a.sinopac_forwarder.OrderID\x1a\x1e.sinopac_forwarder.TradeResult\"\x00\x12U\n\x11GetOrderStatusArr\x12\x16.google.protobuf.Empty\x1a&.sinopac_forwarder.StockOrderStatusArr\"\x00\x12V\n\x19GetNonBlockOrderStatusArr\x12\x16.google.protobuf.Empty\x1a\x1f.sinopac_forwarder.ErrorMessage\"\x00\x12S\n\tBuyFuture\x12$.sinopac_forwarder.FutureOrderDetail\x1a\x1e.sinopac_forwarder.TradeResult\"\x00\x12T\n\nSellFuture\x12$.sinopac_forwarder.FutureOrderDetail\x1a\x1e.sinopac_forwarder.TradeResult\"\x00\x12Y\n\x0fSellFirstFuture\x12$.sinopac_forwarder.FutureOrderDetail\x1a\x1e.sinopac_forwarder.TradeResult\"\x00\x12R\n\x0c\x43\x61ncelFuture\x12 .sinopac_forwarder.FutureOrderID\x1a\x1e.sinopac_forwarder.TradeResult\"\x00\x42\x06Z\x04./pbb\x06proto3')



_STOCKORDERDETAIL = DESCRIPTOR.message_types_by_name['StockOrderDetail']
_FUTUREORDERDETAIL = DESCRIPTOR.message_types_by_name['FutureOrderDetail']
_TRADERESULT = DESCRIPTOR.message_types_by_name['TradeResult']
_ORDERID = DESCRIPTOR.message_types_by_name['OrderID']
_FUTUREORDERID = DESCRIPTOR.message_types_by_name['FutureOrderID']
_STOCKORDERSTATUSARR = DESCRIPTOR.message_types_by_name['StockOrderStatusArr']
_STOCKORDERSTATUS = DESCRIPTOR.message_types_by_name['StockOrderStatus']
StockOrderDetail = _reflection.GeneratedProtocolMessageType('StockOrderDetail', (_message.Message,), {
  'DESCRIPTOR' : _STOCKORDERDETAIL,
  '__module__' : 'pb.trade_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.StockOrderDetail)
  })
_sym_db.RegisterMessage(StockOrderDetail)

FutureOrderDetail = _reflection.GeneratedProtocolMessageType('FutureOrderDetail', (_message.Message,), {
  'DESCRIPTOR' : _FUTUREORDERDETAIL,
  '__module__' : 'pb.trade_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.FutureOrderDetail)
  })
_sym_db.RegisterMessage(FutureOrderDetail)

TradeResult = _reflection.GeneratedProtocolMessageType('TradeResult', (_message.Message,), {
  'DESCRIPTOR' : _TRADERESULT,
  '__module__' : 'pb.trade_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.TradeResult)
  })
_sym_db.RegisterMessage(TradeResult)

OrderID = _reflection.GeneratedProtocolMessageType('OrderID', (_message.Message,), {
  'DESCRIPTOR' : _ORDERID,
  '__module__' : 'pb.trade_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.OrderID)
  })
_sym_db.RegisterMessage(OrderID)

FutureOrderID = _reflection.GeneratedProtocolMessageType('FutureOrderID', (_message.Message,), {
  'DESCRIPTOR' : _FUTUREORDERID,
  '__module__' : 'pb.trade_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.FutureOrderID)
  })
_sym_db.RegisterMessage(FutureOrderID)

StockOrderStatusArr = _reflection.GeneratedProtocolMessageType('StockOrderStatusArr', (_message.Message,), {
  'DESCRIPTOR' : _STOCKORDERSTATUSARR,
  '__module__' : 'pb.trade_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.StockOrderStatusArr)
  })
_sym_db.RegisterMessage(StockOrderStatusArr)

StockOrderStatus = _reflection.GeneratedProtocolMessageType('StockOrderStatus', (_message.Message,), {
  'DESCRIPTOR' : _STOCKORDERSTATUS,
  '__module__' : 'pb.trade_pb2'
  # @@protoc_insertion_point(class_scope:sinopac_forwarder.StockOrderStatus)
  })
_sym_db.RegisterMessage(StockOrderStatus)

_TRADEINTERFACE = DESCRIPTOR.services_by_name['TradeInterface']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\004./pb'
  _STOCKORDERDETAIL._serialized_start=83
  _STOCKORDERDETAIL._serialized_end=171
  _FUTUREORDERDETAIL._serialized_start=173
  _FUTUREORDERDETAIL._serialized_end=239
  _TRADERESULT._serialized_start=241
  _TRADERESULT._serialized_end=303
  _ORDERID._serialized_start=305
  _ORDERID._serialized_end=350
  _FUTUREORDERID._serialized_start=352
  _FUTUREORDERID._serialized_end=385
  _STOCKORDERSTATUSARR._serialized_start=387
  _STOCKORDERSTATUSARR._serialized_end=459
  _STOCKORDERSTATUS._serialized_start=462
  _STOCKORDERSTATUS._serialized_end=597
  _TRADEINTERFACE._serialized_start=600
  _TRADEINTERFACE._serialized_end=1554
# @@protoc_insertion_point(module_scope)
