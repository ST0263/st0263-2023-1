# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Service_pb2 as Service__pb2


class ProductServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddProduct = channel.unary_unary(
                '/ProductService/AddProduct',
                request_serializer=Service__pb2.Product.SerializeToString,
                response_deserializer=Service__pb2.TransactionResponse.FromString,
                )


class ProductServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.AddProduct,
                    request_deserializer=Service__pb2.Product.FromString,
                    response_serializer=Service__pb2.TransactionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProductService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProductService/AddProduct',
            Service__pb2.Product.SerializeToString,
            Service__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
