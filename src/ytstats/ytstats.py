import os

from typing import Dict
from typing import List
from youtube_api import YouTubeDataAPI

api: str = os.environ['APIKEY']


def youtube(self, chans: List[str]) -> List[StatsData]:
    from typing import Dict
    from youtube_api import YouTubeDataAPI

    yt: YouTubeDataAPI = YouTubeDataAPI(self.api, verify_api_key=False, verbose=True)
    body: Dict = yt.get_channel_metadata(channel_id=chans, parser=None, part=['statistics'])

    stats = []
    for s in body:
        serial: str = s['id']
        view: int = int(s['statistics']['viewCount'])
        subs: int = int(s['statistics']['subscriberCount'])
        vids: int = int(s['statistics']['videoCount'])
        stat_obj: YtStats.StatsData = YtStats.StatsData(serial, view, subs, vids)

        stats.append(stat_obj)

    return stats


def main() -> None:
    YtStats.main()


main()
