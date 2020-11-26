class YtStats:
    from typing import List

    class StatsData:
        def __init__(self, serial: str, view: int, subs: int, vids: int):
            import datetime

            self.serial = serial
            self.timestamp = datetime.datetime.now()
            self.view = view
            self.subs = subs
            self.vids = vids


    @staticmethod
    def main() -> None:
        from typing import List

        stub: YtStats = YtStats()
        channels: List[str] =

        YtStats.chan(stub)

    @staticmethod
    def get(key: str) -> str:
        import os
        return os.environ[key]

    def __init__(self):
        self.api: str = YtStats.get('APIKEY')

        self.host: str = YtStats.get('HOST')
        self.port: str = YtStats.get('PORT')
        self.user: str = YtStats.get('USER')
        self.passwd: str = YtStats.get('PASS')

        self.db: str = YtStats.get('DB')
        self.table: str = YtStats.get('TABLE')

    def __repr__(self):
        return "Envy()"

    def __str__(self):
        return f'Envy(api={self.api}, host={self.host}, port={self.port}, user={self.user}, passwd={self.passwd})'

    def get_incumbent_chans(conn):
        postgresql_select_query = 'SELECT id, serial FROM youtube.public.channels ORDER BY id'
        cursor = conn.cursor()
        cursor.execute(postgresql_select_query)
        records = cursor.fetchall()

        ignore = set()
        for i in records:
            ignore.add(i[0])

        print(len(ignore), 'channels from table')

        cursor.close()
        return ignore

    @staticmethod
    def channels(self) -> List[str]:
        import psycopg2

        self: YtStats = self
        user: str = self.user
        password: str = self.passwd
        host: str = self.host
        port: str = self.port

        connection = psycopg2.connect(user='root', password='', host='127.0.0.1', port='5432', database='youtube')

    @staticmethod
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

    def channels(self):


def main() -> None:
    YtStats.main()


main()
