import isodate
import datetime
from src.channel import Channel


class PlayList(Channel):
    def __init__(self, playlist_id, channel_id=''):
        super().__init__(channel_id)
        self.playlist_id = playlist_id
        self.total_duration_seconds = None
        self.formatted_duration = None
        self.get_playlist_info()

    def __str__(self):
        return self.formatted_duration

    def get_playlist_info(self):
        youtube = Channel.get_service()
        playlist_data = youtube.playlists().list(id=self.playlist_id, part='snippet').execute()

        if 'items' in playlist_data and playlist_data['items']:
            playlist_data = playlist_data['items'][0]['snippet']
            self.title = playlist_data['title']
            self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        else:
            print("No playlist data found.")

    @property
    def total_duration(self):
        youtube = Channel.get_service()
        playlist_items = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=self.playlist_id,
            maxResults=50
        ).execute()
        video_ids = [item['contentDetails']['videoId'] for item in playlist_items['items']]
        video_response = youtube.videos().list(
            part='contentDetails',
            id=','.join(video_ids)
        ).execute()
        total_duration_seconds = 0

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration_st = isodate.parse_duration(iso_8601_duration)
            total_duration_seconds += duration_st.total_seconds()

        total_duration_timedelta = datetime.timedelta(seconds=total_duration_seconds)
        hours = int(total_duration_seconds // 3600)
        minutes = int((total_duration_seconds % 3600) // 60)
        seconds = int(total_duration_seconds % 60)
        self.formatted_duration = f'{hours}:{minutes:02}:{seconds:02}'
        return total_duration_timedelta

    def show_best_video(self):
        # возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        pass
