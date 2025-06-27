from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class MediaFile:
    format: str
    filename: str


class IMediaPlayer(ABC):
    @abstractmethod
    def play_audio(self):
        raise NotImplementedError

    @abstractmethod
    def display_video(self):
        raise NotImplementedError

    @abstractmethod
    def view_image(self):
        raise NotImplementedError


class AudioPlayer(IMediaPlayer):
    def play_audio(self):
        # Implementation...
        pass

    def display_video(self):
        raise NotImplementedError

    def view_image(self):
        raise NotImplementedError


class VideoPlayer(IMediaPlayer):
    def play_audio(self):
        raise NotImplementedError

    def display_video(self):
        # Implementation...
        pass

    def view_image(self):
        raise NotImplementedError


class ImagePlayer(IMediaPlayer):
    def play_audio(self):
        raise NotImplementedError

    def display_video(self):
        raise NotImplementedError

    def view_image(self):
        # Implementation...
        pass


class MediaListPlayer:
    def play_list(self, media_list, players):
        for media in media_list:
            # Implementation...
            pass
