import grpc
import logging
import os
import psycopg2

import writer_pb2
import writer_pb2_grpc

from concurrent import futures


logging.basicConfig(level=logging.DEBUG)


class Server(writer_pb2_grpc.WriterServicer):
    def __init__(self):
        self.host = os.environ['HOST']
        self.port = os.environ['PORT']
        self.user = os.environ['USER']
        self.passwd = os.environ['PASS']

        self.db = os.environ['DB']
        self.table = os.environ['TABLE']

    def SayHello(self, request, context):
        logging.info('Got Request')
        print(request)

        return writer_pb2.WriterReply(ack=True)


def serve():
    server_port = int(os.environ['SERVERPORT'])
    logging.info(f'Server up at port {server_port}')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    writer_pb2_grpc.add_WriterServicer_to_server(Server(), server)
    server.add_insecure_port(f'127.0.0.1:{server_port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
