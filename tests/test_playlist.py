from src.playlist import PlayList
from src.channel import Channel


def test_str():
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    duration = pl.total_duration
    assert str(duration) == "1:49:52"

def test_get_playlist_info():
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"


def test_show_best_video():
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"

