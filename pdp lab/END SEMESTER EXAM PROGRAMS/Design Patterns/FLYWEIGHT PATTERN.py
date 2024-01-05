#flyweight pattern
from abc import ABC,abstractmethod

'''The use of a factory in the Flyweight Pattern serves several important purposes:

Centralized Object Creation:

The factory (SongFactory in this case) centralizes the creation of
flyweight objects (shared objects).
It ensures that shared objects are created in a controlled manner,
with the ability to manage their instantiation and reuse.
Avoiding Duplication:

The factory checks if a similar object already
exists before creating a new one. This prevents
the creation of duplicate objects and ensures that shared instances are reused.
Efficient Memory Management:

By centralizing the creation and management of
flyweight objects, the factory contributes to efficient memory usage.
It helps in minimizing the number of instances
of shared objects, reducing the overall memory footprint of the application.'''

#Flyweightinterface
class song(ABC):

    @abstractmethod
    def play(self):
        pass

#Concrete Flyweight
class SharedSong(song):
    def __init__(self,title,artist,album):
        self.title=title
        self.artist=artist
        self.album=album

    def play(self,user_rating):
        print(f' playing the song {self.title} by {self.artist}')
        print(f'song rating {user_rating}') #user_rating is extrinsic changes everytime


#FlyWeightfactory
class SongFactory:

    def __init__(self):
        self.shared_songs={}

    def get_shared_song(self, title, artist, album):
        key = (title, artist, album)
        if key not in self.shared_songs:
            self.shared_songs[key] = SharedSong(title, artist, album)
        return self.shared_songs[key]

# Client
class Playlist:
    def __init__(self, song_factory):
        self.song_factory = song_factory
        self.playlist = []

    def add_song(self, title, artist, album, user_rating):
        shared_song = self.song_factory.get_shared_song(title, artist, album)
        self.playlist.append((shared_song, user_rating))

    def play_playlist(self):
        for shared_song, user_rating in self.playlist:
            shared_song.play(user_rating)

# Client Code
song_factory = SongFactory()
my_playlist = Playlist(song_factory)

my_playlist.add_song("Song1", "Artist1", "Album1", user_rating=4)
my_playlist.add_song("Song2", "Artist2", "Album2", user_rating=5)
my_playlist.add_song("Song1", "Artist1", "Album1", user_rating=3)  # Reusing shared song

my_playlist.play_playlist()


