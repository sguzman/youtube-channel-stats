import grpc
import os
import service_pb2
import service_pb2_grpc

from youtube_api import YouTubeDataAPI

api = os.environ['APIKEY']
port = int(os.environ['QUERYPORT'])
addr = f'localhost:{port}'

if __name__ == '__main__':
    channel = grpc.insecure_channel(addr)
    stub = service_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(service_pb2.HelloRequest(size=50))
    print("Greeter client received:", response.message)

    chans = [x.message for x in response.message]
    dict_chans= {}
    for pair in response.message:
        dict_chans[pair.message] = pair.id

    yt = YouTubeDataAPI(api, verify_api_key=False, verbose=True)
    body = yt.get_channel_metadata(channel_id=chans, parser=None, part=['statistics'])

    stats = []
    for s in body:
        serial = s['id']
        view = int(s['statistics']['viewCount'])
        if s['statistics']['hiddenSubscriberCount']:
            subs = 0
        else:
            subs = int(s['statistics']['subscriberCount'])
        vids = int(s['statistics']['videoCount'])
        stats.append((dict_chans[serial], serial, view, subs, vids))

    print(stats)
