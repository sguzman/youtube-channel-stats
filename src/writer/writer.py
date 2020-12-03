import atexit
import grpc
import logging
import os
import psycopg2

import writer_pb2
import writer_pb2_grpc

from concurrent import futures


logging.basicConfig(level=logging.DEBUG)


class Server(writer_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.host = os.environ['HOST']
        self.port = os.environ['PORT']
        self.user = os.environ['USER']
        self.passwd = os.environ['PASS']

        self.db = os.environ['DB']
        self.table = os.environ['TABLE']

    def SayHello(self, request: writer_pb2.HelloRequest, context):
        logging.info('Got Request')
        conn: psycopg2 = psycopg2.connect(user=self.user, password=self.passwd, host=self.host, port=self.port, database=self.db)

        size = 50 if request.size < 1 or request.size > 50 else request.size
        postgresql_select_query = f'SELECT id, serial FROM {self.table} ORDER BY random() LIMIT {size}'
        cursor = conn.cursor()
        cursor.execute(postgresql_select_query)

        records = cursor.fetchall()
        cursor.close()
        conn.close()

        logging.info(f'Sending data: {records}')
        msg = writer_pb2.HelloReply()
        for pair in records:
            packet = writer_pb2.HelloPacket()
            packet.id = pair[0]
            packet.message = pair[1]
            msg.message.append(packet)

        return msg


def serve():
    server_port = int(os.environ['SERVERPORT'])
    logging.info(f'Server up at port {server_port}')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    writer_pb2_grpc.add_GreeterServicer_to_server(Server(), server)
    server.add_insecure_port(f'[::]:{server_port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
