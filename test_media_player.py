import pytest

from media_player import AudioPlayer, VideoPlayer, ImagePlayer


def test_audio_player():
    audio_player = AudioPlayer()
    audio_player.play_audio()  # No exception should be raised
    with pytest.raises(NotImplementedError):
        audio_player.display_video()
    with pytest.raises(NotImplementedError):
        audio_player.view_image()


def test_video_player():
    video_player = VideoPlayer()
    video_player.display_video()  # No exception should be raised
    with pytest.raises(NotImplementedError):
        video_player.play_audio()
    with pytest.raises(NotImplementedError):
        video_player.view_image()


def test_image_player():
    image_player = ImagePlayer()
    image_player.view_image()  # No exception should be raised
    with pytest.raises(NotImplementedError):
        image_player.play_audio()
    with pytest.raises(NotImplementedError):
        image_player.display_video()
