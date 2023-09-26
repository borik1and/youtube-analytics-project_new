from src.video import Video, PLVideo


def test_get_video_info():
    video1 = Video('AWX4JnAnjBE')
    assert str(video1) == 'GIL в Python: зачем он нужен и как с этим жить'
    assert video1.title == 'GIL в Python: зачем он нужен и как с этим жить'
    assert video1.channel_title == 'MoscowPython'



def test_plvideo():
    video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert str(video2) == 'MoscowPython Meetup 78 - вступление'
