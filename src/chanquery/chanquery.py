import atexit
import grpc
import logging
import os
import psycopg2


import service_pb2
import service_pb2_grpc

from concurrent import futures
from typing import List
from typing import Tuple

logging.basicConfig(level=logging.DEBUG)


class Server(service_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.host: str = os.environ['HOST']
        self.port: str = os.environ['PORT']
        self.user: str = os.environ['USER']
        self.passwd: str = os.environ['PASS']

        self.db: str = os.environ['DB']
        self.table: str = os.environ['TABLE']

    def SayHello(self, request: service_pb2.HelloRequest, context) -> service_pb2.HelloReply:
        logging.info('Got Request')
        conn: psycopg2 = psycopg2.connect(user=self.user, password=self.passwd, host=self.host, port=self.port, database=self.db)

        size: int = 50 if request.size < 1 or request.size > 50 else request.size
        postgresql_select_query: str = f'SELECT id, serial FROM {self.table} ORDER BY random() LIMIT {size}'
        cursor = conn.cursor()
        cursor.execute(postgresql_select_query)

        records: List[Tuple[int,str]] = cursor.fetchall()
        cursor.close()
        conn.close()

        logging.info(f'Sending data: {records}')
        msg: service_pb2.HelloReply = service_pb2.HelloReply()
        for pair in records:
            packet: service_pb2.HelloPacket = service_pb2.HelloPacket()
            packet.id = pair[0]
            packet.message = pair[1]
            msg.message.append(packet)

        return msg


def serve():
    server_port: int = int(os.environ['SERVERPORT'])
    logging.info(f'Server up at port {server_port}')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    service_pb2_grpc.add_GreeterServicer_to_server(Server(), server)
    server.add_insecure_port(f'[::]:{server_port}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()