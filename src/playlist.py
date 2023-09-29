import isodate

from src.channel import Channel


class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.title = None  # Initialize the title attribute

    def get_playlist_info(self):
        youtube = Channel.get_service()
        playlist_data = youtube.playlists().list(id=self.playlist_id, part='snippet').execute()

        if 'items' in playlist_data:
            playlist_data = playlist_data['items'][0]['snippet']
            self.title = playlist_data['title']
            self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"
        else:
            print("No playlist data found.")

    @property
    def total_duration(self):
        youtube = Channel.get_service()
        playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        total_seconds = 0

        if 'items' in playlist_videos:
            for video in playlist_videos['items']:
                content_details = video.get['contentDetails']
                duration_iso = content_details.get['duration']
                duration_seconds = isodate.parse_duration(duration_iso).total_seconds()
                total_seconds += duration_seconds

        return total_seconds

    def show_best_video(self):
        # возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)
        pass
