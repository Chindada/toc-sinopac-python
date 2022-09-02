# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import common_pb2 as pb_dot_common__pb2
import trade_pb2 as pb_dot_trade__pb2


class TradeInterfaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BuyStock = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/BuyStock",
            request_serializer=pb_dot_trade__pb2.StockOrderDetail.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.TradeResult.FromString,
        )
        self.SellStock = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/SellStock",
            request_serializer=pb_dot_trade__pb2.StockOrderDetail.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.TradeResult.FromString,
        )
        self.SellFirstStock = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/SellFirstStock",
            request_serializer=pb_dot_trade__pb2.StockOrderDetail.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.TradeResult.FromString,
        )
        self.CancelStock = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/CancelStock",
            request_serializer=pb_dot_trade__pb2.OrderID.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.TradeResult.FromString,
        )
        self.GetOrderStatusByID = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/GetOrderStatusByID",
            request_serializer=pb_dot_trade__pb2.OrderID.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.TradeResult.FromString,
        )
        self.GetOrderStatusArr = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/GetOrderStatusArr",
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.StockOrderStatusArr.FromString,
        )
        self.GetNonBlockOrderStatusArr = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/GetNonBlockOrderStatusArr",
            request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            response_deserializer=pb_dot_common__pb2.ErrorMessage.FromString,
        )
        self.BuyFuture = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/BuyFuture",
            request_serializer=pb_dot_trade__pb2.FutureOrderDetail.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.TradeResult.FromString,
        )
        self.SellFuture = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/SellFuture",
            request_serializer=pb_dot_trade__pb2.FutureOrderDetail.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.TradeResult.FromString,
        )
        self.SellFirstFuture = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/SellFirstFuture",
            request_serializer=pb_dot_trade__pb2.FutureOrderDetail.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.TradeResult.FromString,
        )
        self.CancelFuture = channel.unary_unary(
            "/sinopac_forwarder.TradeInterface/CancelFuture",
            request_serializer=pb_dot_trade__pb2.FutureOrderID.SerializeToString,
            response_deserializer=pb_dot_trade__pb2.TradeResult.FromString,
        )


class TradeInterfaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BuyStock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SellStock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SellFirstStock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CancelStock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetOrderStatusByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetOrderStatusArr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetNonBlockOrderStatusArr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def BuyFuture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SellFuture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def SellFirstFuture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def CancelFuture(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_TradeInterfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "BuyStock": grpc.unary_unary_rpc_method_handler(
            servicer.BuyStock,
            request_deserializer=pb_dot_trade__pb2.StockOrderDetail.FromString,
            response_serializer=pb_dot_trade__pb2.TradeResult.SerializeToString,
        ),
        "SellStock": grpc.unary_unary_rpc_method_handler(
            servicer.SellStock,
            request_deserializer=pb_dot_trade__pb2.StockOrderDetail.FromString,
            response_serializer=pb_dot_trade__pb2.TradeResult.SerializeToString,
        ),
        "SellFirstStock": grpc.unary_unary_rpc_method_handler(
            servicer.SellFirstStock,
            request_deserializer=pb_dot_trade__pb2.StockOrderDetail.FromString,
            response_serializer=pb_dot_trade__pb2.TradeResult.SerializeToString,
        ),
        "CancelStock": grpc.unary_unary_rpc_method_handler(
            servicer.CancelStock,
            request_deserializer=pb_dot_trade__pb2.OrderID.FromString,
            response_serializer=pb_dot_trade__pb2.TradeResult.SerializeToString,
        ),
        "GetOrderStatusByID": grpc.unary_unary_rpc_method_handler(
            servicer.GetOrderStatusByID,
            request_deserializer=pb_dot_trade__pb2.OrderID.FromString,
            response_serializer=pb_dot_trade__pb2.TradeResult.SerializeToString,
        ),
        "GetOrderStatusArr": grpc.unary_unary_rpc_method_handler(
            servicer.GetOrderStatusArr,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=pb_dot_trade__pb2.StockOrderStatusArr.SerializeToString,
        ),
        "GetNonBlockOrderStatusArr": grpc.unary_unary_rpc_method_handler(
            servicer.GetNonBlockOrderStatusArr,
            request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            response_serializer=pb_dot_common__pb2.ErrorMessage.SerializeToString,
        ),
        "BuyFuture": grpc.unary_unary_rpc_method_handler(
            servicer.BuyFuture,
            request_deserializer=pb_dot_trade__pb2.FutureOrderDetail.FromString,
            response_serializer=pb_dot_trade__pb2.TradeResult.SerializeToString,
        ),
        "SellFuture": grpc.unary_unary_rpc_method_handler(
            servicer.SellFuture,
            request_deserializer=pb_dot_trade__pb2.FutureOrderDetail.FromString,
            response_serializer=pb_dot_trade__pb2.TradeResult.SerializeToString,
        ),
        "SellFirstFuture": grpc.unary_unary_rpc_method_handler(
            servicer.SellFirstFuture,
            request_deserializer=pb_dot_trade__pb2.FutureOrderDetail.FromString,
            response_serializer=pb_dot_trade__pb2.TradeResult.SerializeToString,
        ),
        "CancelFuture": grpc.unary_unary_rpc_method_handler(
            servicer.CancelFuture,
            request_deserializer=pb_dot_trade__pb2.FutureOrderID.FromString,
            response_serializer=pb_dot_trade__pb2.TradeResult.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "sinopac_forwarder.TradeInterface", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class TradeInterface(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BuyStock(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/BuyStock",
            pb_dot_trade__pb2.StockOrderDetail.SerializeToString,
            pb_dot_trade__pb2.TradeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SellStock(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/SellStock",
            pb_dot_trade__pb2.StockOrderDetail.SerializeToString,
            pb_dot_trade__pb2.TradeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SellFirstStock(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/SellFirstStock",
            pb_dot_trade__pb2.StockOrderDetail.SerializeToString,
            pb_dot_trade__pb2.TradeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CancelStock(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/CancelStock",
            pb_dot_trade__pb2.OrderID.SerializeToString,
            pb_dot_trade__pb2.TradeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetOrderStatusByID(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/GetOrderStatusByID",
            pb_dot_trade__pb2.OrderID.SerializeToString,
            pb_dot_trade__pb2.TradeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetOrderStatusArr(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/GetOrderStatusArr",
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pb_dot_trade__pb2.StockOrderStatusArr.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetNonBlockOrderStatusArr(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/GetNonBlockOrderStatusArr",
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pb_dot_common__pb2.ErrorMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def BuyFuture(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/BuyFuture",
            pb_dot_trade__pb2.FutureOrderDetail.SerializeToString,
            pb_dot_trade__pb2.TradeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SellFuture(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/SellFuture",
            pb_dot_trade__pb2.FutureOrderDetail.SerializeToString,
            pb_dot_trade__pb2.TradeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def SellFirstFuture(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/SellFirstFuture",
            pb_dot_trade__pb2.FutureOrderDetail.SerializeToString,
            pb_dot_trade__pb2.TradeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def CancelFuture(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/sinopac_forwarder.TradeInterface/CancelFuture",
            pb_dot_trade__pb2.FutureOrderID.SerializeToString,
            pb_dot_trade__pb2.TradeResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
