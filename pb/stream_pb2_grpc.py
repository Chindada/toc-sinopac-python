# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common_pb2 as common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import stream_pb2 as stream__pb2


class StreamDataInterfaceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStockSnapshotByNumArr = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/GetStockSnapshotByNumArr',
                request_serializer=common__pb2.StockNumArr.SerializeToString,
                response_deserializer=stream__pb2.SnapshotResponse.FromString,
                )
        self.GetAllStockSnapshot = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/GetAllStockSnapshot',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=stream__pb2.SnapshotResponse.FromString,
                )
        self.GetStockSnapshotTSE = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/GetStockSnapshotTSE',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=stream__pb2.SnapshotMessage.FromString,
                )
        self.GetStockVolumeRank = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/GetStockVolumeRank',
                request_serializer=stream__pb2.VolumeRankRequest.SerializeToString,
                response_deserializer=stream__pb2.StockVolumeRankResponse.FromString,
                )
        self.SubscribeStockTick = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/SubscribeStockTick',
                request_serializer=common__pb2.StockNumArr.SerializeToString,
                response_deserializer=stream__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeStockTick = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/UnSubscribeStockTick',
                request_serializer=common__pb2.StockNumArr.SerializeToString,
                response_deserializer=stream__pb2.SubscribeResponse.FromString,
                )
        self.SubscribeStockBidAsk = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/SubscribeStockBidAsk',
                request_serializer=common__pb2.StockNumArr.SerializeToString,
                response_deserializer=stream__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeStockBidAsk = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/UnSubscribeStockBidAsk',
                request_serializer=common__pb2.StockNumArr.SerializeToString,
                response_deserializer=stream__pb2.SubscribeResponse.FromString,
                )
        self.SubscribeFutureTick = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/SubscribeFutureTick',
                request_serializer=common__pb2.FutureCodeArr.SerializeToString,
                response_deserializer=stream__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeFutureTick = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/UnSubscribeFutureTick',
                request_serializer=common__pb2.FutureCodeArr.SerializeToString,
                response_deserializer=stream__pb2.SubscribeResponse.FromString,
                )
        self.UnSubscribeStockAllTick = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/UnSubscribeStockAllTick',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=common__pb2.ErrorMessage.FromString,
                )
        self.UnSubscribeStockAllBidAsk = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/UnSubscribeStockAllBidAsk',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=common__pb2.ErrorMessage.FromString,
                )
        self.GetFutureSnapshotByCodeArr = channel.unary_unary(
                '/sinopac_forwarder.StreamDataInterface/GetFutureSnapshotByCodeArr',
                request_serializer=common__pb2.FutureCodeArr.SerializeToString,
                response_deserializer=stream__pb2.SnapshotResponse.FromString,
                )


class StreamDataInterfaceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStockSnapshotByNumArr(self, request, context):
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

    def SubscribeStockTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeStockTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeStockBidAsk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeStockBidAsk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeFutureTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeFutureTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeStockAllTick(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribeStockAllBidAsk(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFutureSnapshotByCodeArr(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamDataInterfaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStockSnapshotByNumArr': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockSnapshotByNumArr,
                    request_deserializer=common__pb2.StockNumArr.FromString,
                    response_serializer=stream__pb2.SnapshotResponse.SerializeToString,
            ),
            'GetAllStockSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllStockSnapshot,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=stream__pb2.SnapshotResponse.SerializeToString,
            ),
            'GetStockSnapshotTSE': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockSnapshotTSE,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=stream__pb2.SnapshotMessage.SerializeToString,
            ),
            'GetStockVolumeRank': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStockVolumeRank,
                    request_deserializer=stream__pb2.VolumeRankRequest.FromString,
                    response_serializer=stream__pb2.StockVolumeRankResponse.SerializeToString,
            ),
            'SubscribeStockTick': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeStockTick,
                    request_deserializer=common__pb2.StockNumArr.FromString,
                    response_serializer=stream__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeStockTick': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeStockTick,
                    request_deserializer=common__pb2.StockNumArr.FromString,
                    response_serializer=stream__pb2.SubscribeResponse.SerializeToString,
            ),
            'SubscribeStockBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeStockBidAsk,
                    request_deserializer=common__pb2.StockNumArr.FromString,
                    response_serializer=stream__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeStockBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeStockBidAsk,
                    request_deserializer=common__pb2.StockNumArr.FromString,
                    response_serializer=stream__pb2.SubscribeResponse.SerializeToString,
            ),
            'SubscribeFutureTick': grpc.unary_unary_rpc_method_handler(
                    servicer.SubscribeFutureTick,
                    request_deserializer=common__pb2.FutureCodeArr.FromString,
                    response_serializer=stream__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeFutureTick': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeFutureTick,
                    request_deserializer=common__pb2.FutureCodeArr.FromString,
                    response_serializer=stream__pb2.SubscribeResponse.SerializeToString,
            ),
            'UnSubscribeStockAllTick': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeStockAllTick,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=common__pb2.ErrorMessage.SerializeToString,
            ),
            'UnSubscribeStockAllBidAsk': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribeStockAllBidAsk,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=common__pb2.ErrorMessage.SerializeToString,
            ),
            'GetFutureSnapshotByCodeArr': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFutureSnapshotByCodeArr,
                    request_deserializer=common__pb2.FutureCodeArr.FromString,
                    response_serializer=stream__pb2.SnapshotResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sinopac_forwarder.StreamDataInterface', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamDataInterface(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/GetStockSnapshotByNumArr',
            common__pb2.StockNumArr.SerializeToString,
            stream__pb2.SnapshotResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/GetAllStockSnapshot',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            stream__pb2.SnapshotResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/GetStockSnapshotTSE',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            stream__pb2.SnapshotMessage.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/GetStockVolumeRank',
            stream__pb2.VolumeRankRequest.SerializeToString,
            stream__pb2.StockVolumeRankResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/SubscribeStockTick',
            common__pb2.StockNumArr.SerializeToString,
            stream__pb2.SubscribeResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/UnSubscribeStockTick',
            common__pb2.StockNumArr.SerializeToString,
            stream__pb2.SubscribeResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/SubscribeStockBidAsk',
            common__pb2.StockNumArr.SerializeToString,
            stream__pb2.SubscribeResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/UnSubscribeStockBidAsk',
            common__pb2.StockNumArr.SerializeToString,
            stream__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeFutureTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/SubscribeFutureTick',
            common__pb2.FutureCodeArr.SerializeToString,
            stream__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeFutureTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/UnSubscribeFutureTick',
            common__pb2.FutureCodeArr.SerializeToString,
            stream__pb2.SubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeStockAllTick(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/UnSubscribeStockAllTick',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            common__pb2.ErrorMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribeStockAllBidAsk(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/UnSubscribeStockAllBidAsk',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            common__pb2.ErrorMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFutureSnapshotByCodeArr(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sinopac_forwarder.StreamDataInterface/GetFutureSnapshotByCodeArr',
            common__pb2.FutureCodeArr.SerializeToString,
            stream__pb2.SnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
