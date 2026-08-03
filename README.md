# Media player refactoring kata in Python

[![CI](https://github.com/Coding-Cuddles/media-player-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/media-player-refactoring-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

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
`IAudioPlayer`, `IVideoPlayer`, and `IImagePlayer` interfaces, each with a
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
of `IAudioPlayer`, `IVideoPlayer`, and `IImagePlayer` instead of
`IMediaPlayer`.

In the `play_list` method, we should use the appropriate player based on the
type of the media file. This may require additional checks or mappings from
file type to player.

Your task is to refactor the code to segregate interfaces based on the
different file formats and adapt the `MediaListPlayer` to work with the new
classes and interfaces.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/media-player-refactoring-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd media-player-refactoring-python-kata
   ```

3. Run the existing tests. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest test_*.py
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `3 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

1. Start Exercise 1 in `media_player.py`. Update `test_media_player.py` as you add behavior.

2. Run the tests after each change. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest test_*.py
   ```

   Continue when the test run passes.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the command reference              |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |
