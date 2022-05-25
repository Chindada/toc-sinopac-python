# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import sinopac_forwarder_pb2 as sinopac__forwarder__pb2


class SinopacForwarderStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetServerToken = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/GetServerToken',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.TokenResponse.FromString,
                )
        self.GetAllStockDetail = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/GetAllStockDetail',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.StockDetailResponse.FromString,
                )
        self.GetAllStockSnapshot = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/GetAllStockSnapshot',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.StockSnapshotResponse.FromString,
                )
        self.GetStockSnapshotTSE = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/GetStockSnapshotTSE',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.StockSnapshotResponse.FromString,
                )
        self.GetStockVolumeRank = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/GetStockVolumeRank',
                request_serializer=sinopac__forwarder__pb2.VolumeRankRequest.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.StockVolumeRankResponse.FromString,
                )
        self.GetStockSnapshotByNumArr = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/GetStockSnapshotByNumArr',
                request_serializer=sinopac__forwarder__pb2.StockNumArr.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.StockSnapshotResponse.FromString,
                )
        self.GetStockHistoryTick = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/GetStockHistoryTick',
                request_serializer=sinopac__forwarder__pb2.StockNumArrWithDate.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.StockHistoryTickResponse.FromString,
                )
        self.GetStockHistoryKbar = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/GetStockHistoryKbar',
                request_serializer=sinopac__forwarder__pb2.StockNumArrWithDate.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.StockHistoryKbarResponse.FromString,
                )
        self.GetStockHistoryClose = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/GetStockHistoryClose',
                request_serializer=sinopac__forwarder__pb2.StockNumArrWithDate.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.StockHistoryCloseResponse.FromString,
                )
        self.SubscribeStockTick = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/SubscribeStockTick',
                request_serializer=sinopac__forwarder__pb2.StockNumArr.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.SubscribeResponse.FromString,
                )
        self.SubscribeStockBidAsk = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/SubscribeStockBidAsk',
                request_serializer=sinopac__forwarder__pb2.StockNumArr.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeStockTick = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/UnSubscribeStockTick',
                request_serializer=sinopac__forwarder__pb2.StockNumArr.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeStockBidAsk = channel.unary_unary(
                '/sinopac_forwarder.SinopacForwarder/UnSubscribeStockBidAsk',
                request_serializer=sinopac__forwarder__pb2.StockNumArr.SerializeToString,
                response_deserializer=sinopac__forwarder__pb2.SubscribeResponse.FromString,
                )


class SinopacForwarderServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetServerToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllStockDetail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllStockSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockSnapshotTSE(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockVolumeRank(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockSnapshotByNumArr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockHistoryTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockHistoryKbar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStockHistoryClose(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeStockTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeStockBidAsk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeStockTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeStockBidAsk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SinopacForwarderServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetServerToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerToken,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=sinopac__forwarder__pb2.TokenResponse.SerializeToString,
            ),
            'GetAllStockDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllStockDetail,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=sinopac__forwarder__pb2.StockDetailResponse.SerializeToString,
            ),
            'GetAllStockSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllStockSnapshot,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=sinopac__forwarder__pb2.StockSnapshotResponse.SerializeToString,
            ),
            'GetStockSnapshotTSE': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockSnapshotTSE,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=sinopac__forwarder__pb2.StockSnapshotResponse.SerializeToString,
            ),
            'GetStockVolumeRank': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockVolumeRank,
                    request_deserializer=sinopac__forwarder__pb2.VolumeRankRequest.FromString,
                    response_serializer=sinopac__forwarder__pb2.StockVolumeRankResponse.SerializeToString,
            ),
            'GetStockSnapshotByNumArr': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockSnapshotByNumArr,
                    request_deserializer=sinopac__forwarder__pb2.StockNumArr.FromString,
                    response_serializer=sinopac__forwarder__pb2.StockSnapshotResponse.SerializeToString,
            ),
            'GetStockHistoryTick': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryTick,
                    request_deserializer=sinopac__forwarder__pb2.StockNumArrWithDate.FromString,
                    response_serializer=sinopac__forwarder__pb2.StockHistoryTickResponse.SerializeToString,
            ),
            'GetStockHistoryKbar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryKbar,
                    request_deserializer=sinopac__forwarder__pb2.StockNumArrWithDate.FromString,
                    response_serializer=sinopac__forwarder__pb2.StockHistoryKbarResponse.SerializeToString,
            ),
            'GetStockHistoryClose': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockHistoryClose,
                    request_deserializer=sinopac__forwarder__pb2.StockNumArrWithDate.FromString,
                    response_serializer=sinopac__forwarder__pb2.StockHistoryCloseResponse.SerializeToString,
            ),
            'SubscribeStockTick': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeStockTick,
                    request_deserializer=sinopac__forwarder__pb2.StockNumArr.FromString,
                    response_serializer=sinopac__forwarder__pb2.SubscribeResponse.SerializeToString,
            ),
            'SubscribeStockBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeStockBidAsk,
                    request_deserializer=sinopac__forwarder__pb2.StockNumArr.FromString,
                    response_serializer=sinopac__forwarder__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeStockTick': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeStockTick,
                    request_deserializer=sinopac__forwarder__pb2.StockNumArr.FromString,
                    response_serializer=sinopac__forwarder__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeStockBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeStockBidAsk,
                    request_deserializer=sinopac__forwarder__pb2.StockNumArr.FromString,
                    response_serializer=sinopac__forwarder__pb2.SubscribeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sinopac_forwarder.SinopacForwarder', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SinopacForwarder(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetServerToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/GetServerToken',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            sinopac__forwarder__pb2.TokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllStockDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/GetAllStockDetail',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            sinopac__forwarder__pb2.StockDetailResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllStockSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/GetAllStockSnapshot',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            sinopac__forwarder__pb2.StockSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockSnapshotTSE(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/GetStockSnapshotTSE',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            sinopac__forwarder__pb2.StockSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockVolumeRank(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/GetStockVolumeRank',
            sinopac__forwarder__pb2.VolumeRankRequest.SerializeToString,
            sinopac__forwarder__pb2.StockVolumeRankResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockSnapshotByNumArr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/GetStockSnapshotByNumArr',
            sinopac__forwarder__pb2.StockNumArr.SerializeToString,
            sinopac__forwarder__pb2.StockSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockHistoryTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/GetStockHistoryTick',
            sinopac__forwarder__pb2.StockNumArrWithDate.SerializeToString,
            sinopac__forwarder__pb2.StockHistoryTickResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockHistoryKbar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/GetStockHistoryKbar',
            sinopac__forwarder__pb2.StockNumArrWithDate.SerializeToString,
            sinopac__forwarder__pb2.StockHistoryKbarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStockHistoryClose(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/GetStockHistoryClose',
            sinopac__forwarder__pb2.StockNumArrWithDate.SerializeToString,
            sinopac__forwarder__pb2.StockHistoryCloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeStockTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/SubscribeStockTick',
            sinopac__forwarder__pb2.StockNumArr.SerializeToString,
            sinopac__forwarder__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeStockBidAsk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/SubscribeStockBidAsk',
            sinopac__forwarder__pb2.StockNumArr.SerializeToString,
            sinopac__forwarder__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeStockTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/UnSubscribeStockTick',
            sinopac__forwarder__pb2.StockNumArr.SerializeToString,
            sinopac__forwarder__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeStockBidAsk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.SinopacForwarder/UnSubscribeStockBidAsk',
            sinopac__forwarder__pb2.StockNumArr.SerializeToString,
            sinopac__forwarder__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
