# Media Player Refactoring Python Kata

[![CI](https://github.com/Coding-Cuddles/media-player-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/media-player-refactoring-python-kata/actions/workflows/main.yml)
[![Replit](https://replit.com/badge?caption=Try%20with%20Replit&variant=small)](https://replit.com/new/github/Coding-Cuddles/media-player-refactoring-python-kata)

## Overview

This kata complements [Clean Code: SOLID, Ep. 12 - Interface Segregation Principle](https://cleancoders.com/episode/clean-code-episode-12).

The exercise involves refactoring a multimedia player system to adhere to this
principle.

The problem we have at hand involves different types of media -- audio, video,
and images. We start with a monolithic `IMediaPlayer` interface that handles
all types of media. This will be your starting point.

## Instructions

### Exercise 1

In the first part, your task is to refactor the existing code such that each
type of media player (audio, video, and image) has its own specific interface,
instead of the monolithic `IMediaPlayer` interface. You should create
`IAudioPlayer`, `IVideoPlayer`, and `IImageViewer` interfaces, each with a
relevant method, and update the `AudioPlayer`, `VideoPlayer`, and `ImagePlayer`
classes to implement these new interfaces.

This part includes unit tests that ensure each type of media player is
functioning correctly. After you have completed your refactoring, all unit
tests should pass.

### Exercise 2

In the second part, we will deal with the compatibility of different players
with different file types.

Before, we had a separate player for each media type. We want to have media
files that come in different formats (e.g., `.mp3`, `.flac`, `.wav` for audio,
`.jpeg`, `.png` for images, and `.mp4`, `.mkv` for videos). And some players
can only handle certain formats.

We have the `MediaFile` class to represent a media file, your task is to:

1. Update the player interfaces to take `MediaFile` objects, e.g.:

    ```python
    class IMediaPlayer(ABC):

        @abstractmethod
        def play_audio(self, file):
            pass
    ```

2. Create specialized players that can only handle certain formats (i.e.,
   `Mp3Player`, `FlacPlayer`, `WavPlayer`).

    ```python
    class Mp3Player(IAudioPlayer):

        def play_audio(file):
            if file.format != "mp3":
                raise ValueError("Invalid file format for Mp3Player!")

            # Implementation...
    ```

   The same kind of specialization will be done for `FlacPlayer`, `WavPlayer`,
   and respective video and image players.

3. Add corresponding unit tests, e.g.:

    ```python
    def test_mp3_player_handles_mp3():
        mp3_player = Mp3Player()
        mp3_file = MediaFile(format="mp3", filename="")
        mp3_player.play_audio(mp3_file)

    def test_mp3_player_rejects_non_mp3():
        mp3_player = Mp3Player()
        flac_file = MediaFile(format="flac", filename="")
        with pytest.raises(ValueError):
            mp3_player.play_audio(flac_file)
    ```

### Exercise 3

In the third part, we introduce the concept of a `MediaListPlayer`. This class
accepts a list of media files and a corresponding list of players. It checks if
the player is compatible with the media file format before trying to
play/display the file.

For the `MediaListPlayer`, we can update the `play_list` method to take a list
of `IAudioPlayer`, `IVideoPlayer`, and `IImageViewer` instead of
`IMediaPlayer`.

In the `play_list` method, we should use the appropriate player based on the
type of the media file. This may require additional checks or mappings from
file type to player.

Your task is to refactor the code to segregate interfaces based on the
different file formats and adapt the `MediaListPlayer` to work with the new
classes and interfaces.

## Usage

You can import this project into [Replit](https://replit.com), and it will
handle all dependencies automatically.

### Prerequisites

* [Python 3.8+](https://www.python.org/)
* [pytest](https://pytest.org)

### Run main

```console
make run
```

### Run tests

```console
make test
```
