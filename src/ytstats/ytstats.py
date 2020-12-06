import datetime
import grpc
import os
import service_pb2
import service_pb2_grpc
import writer_pb2
import writer_pb2_grpc

from youtube_api import YouTubeDataAPI

api = os.environ['APIKEY']
port = int(os.environ['QUERYPORT'])
addr = f'localhost:{port}'
port2 = int(os.environ['WRITEPORT'])
addr2 = f'localhost:{port2}'

if __name__ == '__main__':
    channel = grpc.insecure_channel(addr)
    stub = service_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(service_pb2.HelloRequest(size=50))

    chans = [x.message for x in response.message]
    dict_chans= {}
    for pair in response.message:
        dict_chans[pair.message] = pair.id

    yt = YouTubeDataAPI(api, verify_api_key=False, verbose=True)
    body = yt.get_channel_metadata(channel_id=chans, parser=None, part=['statistics'])

    request_body = writer_pb2.WriterRequest()
    for s in body:
        packet = writer_pb2.WriterPacket()
        serial = s['id']
        view = int(s['statistics']['viewCount'])
        if s['statistics']['hiddenSubscriberCount']:
            subs = 0
        else:
            subs = int(s['statistics']['subscriberCount'])
        vids = int(s['statistics']['videoCount'])
        packet.id = dict_chans[serial]
        packet.subs = subs
        packet.views = view
        packet.vids = vids
        request_body.packet.append(packet)

    channel2 = grpc.insecure_channel(addr2)
    stub2 = writer_pb2_grpc.WriterStub(channel2)
    response2 = stub2.SayHello(request_body)
    print("Greeter client received:", response2)
