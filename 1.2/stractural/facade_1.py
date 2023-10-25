
class VideoFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print("Decoding video file:", self.filename)


class AudioFile:
    def __init__(self, filename):
        self.filename = filename

    def decode(self):
        print("Decoding audio file:", self.filename)


class SubtitleFile:
    def __init__(self, filename):
        self.filename = filename

    def show(self):
        print("Decoding subtitle file:", self.filename)


class VideoPlayerFacade:
    def __init__(self, video_file, audio_file, subtitle_file=None):
        self.video_file = video_file
        self.audio_file = audio_file
        self.subtitle_file = subtitle_file

    def play(self):
        self.video_file.decode()
        self.audio_file.decode()
        if self.subtitle_file:
            self.subtitle_file.show()


if __name__ == '__main__':
    video_file = VideoFile("action_movie.mp4")
    audio_file = AudioFile("action_movie.mp3")
    subtitle_file = SubtitleFile("action_movie.srt")

    player = VideoPlayerFacade(video_file, audio_file, subtitle_file)
    player.play()
