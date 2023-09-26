from src.channel import Channel


class Video(Channel):
    def __init__(self, video_id, channel_id=''):
        super().__init__(channel_id)
        self.video_id = video_id
        self.title = None
        self.channel_title = None
        self.description = None
        self.get_video_info()

    def get_video_info(self):
        # открытие видео по id
        youtube = Channel.get_service()
        video_data = youtube.videos().list(part='snippet', id=self.video_id).execute()

        # проверка существования видео
        if 'items' in video_data:
            video = video_data['items'][0]
            self.title = video['snippet']['title']  # Store video title
            self.channel_title = video['snippet']['channelTitle']  # Store channel title
            self.description = video['snippet']['description']  # Store description
        else:
            print("Видео не найдено!plvideo")

    def __str__(self):
        # возвращает название видео
        return self.title


class PLVideo(Video):
    def __init__(self, channel_id, id_video):
        super().__init__(channel_id)
        self.id_video = id_video

    # def __str__(self):
    #     # возвращает название видео и канала
    #     return self.title
