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

class VolumeRankRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COUNT_FIELD_NUMBER: builtins.int
    DATE_FIELD_NUMBER: builtins.int
    count: builtins.int
    date: builtins.str
    def __init__(
        self,
        *,
        count: builtins.int = ...,
        date: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["count", b"count", "date", b"date"]) -> None: ...

global___VolumeRankRequest = VolumeRankRequest

class SnapshotResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SnapshotMessage]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[global___SnapshotMessage] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___SnapshotResponse = SnapshotResponse

class SnapshotMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TS_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    EXCHANGE_FIELD_NUMBER: builtins.int
    OPEN_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    LOW_FIELD_NUMBER: builtins.int
    CLOSE_FIELD_NUMBER: builtins.int
    TICK_TYPE_FIELD_NUMBER: builtins.int
    CHANGE_PRICE_FIELD_NUMBER: builtins.int
    CHANGE_RATE_FIELD_NUMBER: builtins.int
    CHANGE_TYPE_FIELD_NUMBER: builtins.int
    AVERAGE_PRICE_FIELD_NUMBER: builtins.int
    VOLUME_FIELD_NUMBER: builtins.int
    TOTAL_VOLUME_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    TOTAL_AMOUNT_FIELD_NUMBER: builtins.int
    YESTERDAY_VOLUME_FIELD_NUMBER: builtins.int
    BUY_PRICE_FIELD_NUMBER: builtins.int
    BUY_VOLUME_FIELD_NUMBER: builtins.int
    SELL_PRICE_FIELD_NUMBER: builtins.int
    SELL_VOLUME_FIELD_NUMBER: builtins.int
    VOLUME_RATIO_FIELD_NUMBER: builtins.int
    ts: builtins.int
    code: builtins.str
    exchange: builtins.str
    open: builtins.float
    high: builtins.float
    low: builtins.float
    close: builtins.float
    tick_type: builtins.str
    change_price: builtins.float
    change_rate: builtins.float
    change_type: builtins.str
    average_price: builtins.float
    volume: builtins.int
    total_volume: builtins.int
    amount: builtins.int
    total_amount: builtins.int
    yesterday_volume: builtins.float
    buy_price: builtins.float
    buy_volume: builtins.float
    sell_price: builtins.float
    sell_volume: builtins.int
    volume_ratio: builtins.float
    def __init__(
        self,
        *,
        ts: builtins.int = ...,
        code: builtins.str = ...,
        exchange: builtins.str = ...,
        open: builtins.float = ...,
        high: builtins.float = ...,
        low: builtins.float = ...,
        close: builtins.float = ...,
        tick_type: builtins.str = ...,
        change_price: builtins.float = ...,
        change_rate: builtins.float = ...,
        change_type: builtins.str = ...,
        average_price: builtins.float = ...,
        volume: builtins.int = ...,
        total_volume: builtins.int = ...,
        amount: builtins.int = ...,
        total_amount: builtins.int = ...,
        yesterday_volume: builtins.float = ...,
        buy_price: builtins.float = ...,
        buy_volume: builtins.float = ...,
        sell_price: builtins.float = ...,
        sell_volume: builtins.int = ...,
        volume_ratio: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "average_price", b"average_price", "buy_price", b"buy_price", "buy_volume", b"buy_volume", "change_price", b"change_price", "change_rate", b"change_rate", "change_type", b"change_type", "close", b"close", "code", b"code", "exchange", b"exchange", "high", b"high", "low", b"low", "open", b"open", "sell_price", b"sell_price", "sell_volume", b"sell_volume", "tick_type", b"tick_type", "total_amount", b"total_amount", "total_volume", b"total_volume", "ts", b"ts", "volume", b"volume", "volume_ratio", b"volume_ratio", "yesterday_volume", b"yesterday_volume"]) -> None: ...

global___SnapshotMessage = SnapshotMessage

class StockVolumeRankResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_FIELD_NUMBER: builtins.int
    @property
    def data(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StockVolumeRankMessage]: ...
    def __init__(
        self,
        *,
        data: collections.abc.Iterable[global___StockVolumeRankMessage] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["data", b"data"]) -> None: ...

global___StockVolumeRankResponse = StockVolumeRankResponse

class StockVolumeRankMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATE_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TS_FIELD_NUMBER: builtins.int
    OPEN_FIELD_NUMBER: builtins.int
    HIGH_FIELD_NUMBER: builtins.int
    LOW_FIELD_NUMBER: builtins.int
    CLOSE_FIELD_NUMBER: builtins.int
    PRICE_RANGE_FIELD_NUMBER: builtins.int
    TICK_TYPE_FIELD_NUMBER: builtins.int
    CHANGE_PRICE_FIELD_NUMBER: builtins.int
    CHANGE_TYPE_FIELD_NUMBER: builtins.int
    AVERAGE_PRICE_FIELD_NUMBER: builtins.int
    VOLUME_FIELD_NUMBER: builtins.int
    TOTAL_VOLUME_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    TOTAL_AMOUNT_FIELD_NUMBER: builtins.int
    YESTERDAY_VOLUME_FIELD_NUMBER: builtins.int
    VOLUME_RATIO_FIELD_NUMBER: builtins.int
    BUY_PRICE_FIELD_NUMBER: builtins.int
    BUY_VOLUME_FIELD_NUMBER: builtins.int
    SELL_PRICE_FIELD_NUMBER: builtins.int
    SELL_VOLUME_FIELD_NUMBER: builtins.int
    BID_ORDERS_FIELD_NUMBER: builtins.int
    BID_VOLUMES_FIELD_NUMBER: builtins.int
    ASK_ORDERS_FIELD_NUMBER: builtins.int
    ASK_VOLUMES_FIELD_NUMBER: builtins.int
    date: builtins.str
    code: builtins.str
    name: builtins.str
    ts: builtins.int
    open: builtins.float
    high: builtins.float
    low: builtins.float
    close: builtins.float
    price_range: builtins.float
    tick_type: builtins.int
    change_price: builtins.float
    change_type: builtins.int
    average_price: builtins.float
    volume: builtins.int
    total_volume: builtins.int
    amount: builtins.int
    total_amount: builtins.int
    yesterday_volume: builtins.int
    volume_ratio: builtins.float
    buy_price: builtins.float
    buy_volume: builtins.int
    sell_price: builtins.float
    sell_volume: builtins.int
    bid_orders: builtins.int
    bid_volumes: builtins.int
    ask_orders: builtins.int
    ask_volumes: builtins.int
    def __init__(
        self,
        *,
        date: builtins.str = ...,
        code: builtins.str = ...,
        name: builtins.str = ...,
        ts: builtins.int = ...,
        open: builtins.float = ...,
        high: builtins.float = ...,
        low: builtins.float = ...,
        close: builtins.float = ...,
        price_range: builtins.float = ...,
        tick_type: builtins.int = ...,
        change_price: builtins.float = ...,
        change_type: builtins.int = ...,
        average_price: builtins.float = ...,
        volume: builtins.int = ...,
        total_volume: builtins.int = ...,
        amount: builtins.int = ...,
        total_amount: builtins.int = ...,
        yesterday_volume: builtins.int = ...,
        volume_ratio: builtins.float = ...,
        buy_price: builtins.float = ...,
        buy_volume: builtins.int = ...,
        sell_price: builtins.float = ...,
        sell_volume: builtins.int = ...,
        bid_orders: builtins.int = ...,
        bid_volumes: builtins.int = ...,
        ask_orders: builtins.int = ...,
        ask_volumes: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "ask_orders", b"ask_orders", "ask_volumes", b"ask_volumes", "average_price", b"average_price", "bid_orders", b"bid_orders", "bid_volumes", b"bid_volumes", "buy_price", b"buy_price", "buy_volume", b"buy_volume", "change_price", b"change_price", "change_type", b"change_type", "close", b"close", "code", b"code", "date", b"date", "high", b"high", "low", b"low", "name", b"name", "open", b"open", "price_range", b"price_range", "sell_price", b"sell_price", "sell_volume", b"sell_volume", "tick_type", b"tick_type", "total_amount", b"total_amount", "total_volume", b"total_volume", "ts", b"ts", "volume", b"volume", "volume_ratio", b"volume_ratio", "yesterday_volume", b"yesterday_volume"]) -> None: ...

global___StockVolumeRankMessage = StockVolumeRankMessage

class SubscribeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FAIL_ARR_FIELD_NUMBER: builtins.int
    @property
    def fail_arr(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        fail_arr: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fail_arr", b"fail_arr"]) -> None: ...

global___SubscribeResponse = SubscribeResponse
