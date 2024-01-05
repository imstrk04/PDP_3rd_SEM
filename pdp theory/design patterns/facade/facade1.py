# Subsystem Classes
class AudioPlayer:
    def play_audio(self):
        print("Playing audio")

class VideoPlayer:
    def play_video(self):
        print("Playing video")

class Projector:
    def display(self):
        print("Displaying on projector")

# Facade
class MultimediaFacade:
    def __init__(self):
        self.audio_player = AudioPlayer()
        self.video_player = VideoPlayer()
        self.projector = Projector()

    def play_movie(self):
        print("------ Playing Movie ------")
        self.audio_player.play_audio()
        self.video_player.play_video()
        self.projector.display()
        print("------ Movie Finished ------")

# Client Code
if __name__ == "__main__":
    multimedia_facade = MultimediaFacade()

    # Client interacts with the simplified interface provided by the Facade
    multimedia_facade.play_movie()
