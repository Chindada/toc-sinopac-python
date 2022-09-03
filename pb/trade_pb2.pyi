"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class StockOrderDetail(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STOCK_NUM_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    SIMULATE_FIELD_NUMBER: builtins.int
    stock_num: builtins.str
    price: builtins.float
    quantity: builtins.int
    simulate: builtins.bool
    def __init__(
        self,
        *,
        stock_num: builtins.str = ...,
        price: builtins.float = ...,
        quantity: builtins.int = ...,
        simulate: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["price", b"price", "quantity", b"quantity", "simulate", b"simulate", "stock_num", b"stock_num"]) -> None: ...

global___StockOrderDetail = StockOrderDetail

class FutureOrderDetail(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    SIMULATE_FIELD_NUMBER: builtins.int
    code: builtins.str
    price: builtins.float
    quantity: builtins.int
    simulate: builtins.bool
    def __init__(
        self,
        *,
        code: builtins.str = ...,
        price: builtins.float = ...,
        quantity: builtins.int = ...,
        simulate: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["code", b"code", "price", b"price", "quantity", b"quantity", "simulate", b"simulate"]) -> None: ...

global___FutureOrderDetail = FutureOrderDetail

class TradeResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORDER_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    order_id: builtins.str
    status: builtins.str
    error: builtins.str
    def __init__(
        self,
        *,
        order_id: builtins.str = ...,
        status: builtins.str = ...,
        error: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["error", b"error", "order_id", b"order_id", "status", b"status"]) -> None: ...

global___TradeResult = TradeResult

class OrderID(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORDER_ID_FIELD_NUMBER: builtins.int
    SIMULATE_FIELD_NUMBER: builtins.int
    order_id: builtins.str
    simulate: builtins.bool
    def __init__(
        self,
        *,
        order_id: builtins.str = ...,
        simulate: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["order_id", b"order_id", "simulate", b"simulate"]) -> None: ...

global___OrderID = OrderID

class FutureOrderID(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORDER_ID_FIELD_NUMBER: builtins.int
    SIMULATE_FIELD_NUMBER: builtins.int
    order_id: builtins.str
    simulate: builtins.bool
    def __init__(
        self,
        *,
        order_id: builtins.str = ...,
        simulate: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["order_id", b"order_id", "simulate", b"simulate"]) -> None: ...

global___FutureOrderID = FutureOrderID

class StockOrderStatusArr(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StockOrderStatus]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[global___StockOrderStatus] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___StockOrderStatusArr = StockOrderStatusArr

class StockOrderStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    PRICE_FIELD_NUMBER: builtins.int
    QUANTITY_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    ORDER_TIME_FIELD_NUMBER: builtins.int
    status: builtins.str
    code: builtins.str
    action: builtins.str
    price: builtins.float
    quantity: builtins.int
    order_id: builtins.str
    order_time: builtins.str
    def __init__(
        self,
        *,
        status: builtins.str = ...,
        code: builtins.str = ...,
        action: builtins.str = ...,
        price: builtins.float = ...,
        quantity: builtins.int = ...,
        order_id: builtins.str = ...,
        order_time: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["action", b"action", "code", b"code", "order_id", b"order_id", "order_time", b"order_time", "price", b"price", "quantity", b"quantity", "status", b"status"]) -> None: ...

global___StockOrderStatus = StockOrderStatus
