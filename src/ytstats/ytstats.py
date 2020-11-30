import grpc
import os
import service_pb2
import service_pb2_grpc

from typing import Dict
from typing import List
from youtube_api import YouTubeDataAPI

api: str = os.environ['APIKEY']
port: int = int(os.environ['QUERYPORT'])
addr: str = f'localhost:{port}'


def get():
    channel: grpc.Channel = grpc.insecure_channel(addr)
    stub: service_pb2_grpc.GreeterStub = service_pb2_grpc.GreeterStub(channel)
    response: service_pb2.HelloReply = stub.SayHello(service_pb2.HelloRequest(size=50))
    print("Greeter client received:", response.message)


if __name__ == '__main__':
    get()
