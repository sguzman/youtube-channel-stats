from typing import Optional


class Stats:
    def __init__(self, view: int, subs: int, vids: int):
        self.view = view
        self.subs = subs
        self.vids = vids


class Envy:
    from typing import List

    @staticmethod
    def get(key: str) -> str:
        import os
        return os.environ[key]

    def __init__(self):
        self.api = Envy.get('APIKEY')

        self.host = Envy.get('HOST')
        self.port = Envy.get('PORT')
        self.user = Envy.get('USER')
        self.passwd = Envy.get('PASS')

    def __repr__(self):
        return "Envy()"

    def __str__(self):
        return f'Envy(api={self.api}, host={self.host}, port={self.port}, user={self.user}, passwd={self.passwd})'

    def chan(self, chans: List[str] = ['UC-9-kyTW8ZkZNDHQJ6FgpwQ', 'UCq-Fj5jknLsUf-MWSy4_brA']) -> List[Stats]:
        from typing import Dict
        from youtube_api import YouTubeDataAPI

        yt: YouTubeDataAPI = YouTubeDataAPI(self.api, verify_api_key=False, verbose=True)
        body: Dict = yt.get_channel_metadata(channel_id=chans, parser=None, part=['statistics'])

        stats = []
        for s in body:
            view: int = int(s['statistics']['viewCount'])
            subs: int = int(s['statistics']['subscriberCount'])
            vids: int = int(s['statistics']['videoCount'])
            stat_obj: Stats = Stats(view, subs, vids)

            stats.append(stat_obj)

        return stats


glbl: Optional[Envy] = None


def init() -> None:
    global glbl
    glbl = Envy()


def main() -> None:
    init()

    print(glbl.chan())


main()
