# TODO: Define a class for MusicPlayer.
# It should encapsulate its attributes and provide methods for
# - adding tracks to the library
# - playing the current track
# - stopping music
# - changing the current track (the new track is provided by the name)
# - retrieving the list of tracks
class MusicPlayer:
    def __init__(self):
        self.__tlist = list()
        self.__current_track = 0
    def add_tracks(self, track):
        self.__tlist.append(track)
    def play_tracks(self, current_track):
        self.__current_track = current_track
        if self.__tlist and len(self.__tlist) > self.__current_track:
            print(f"playing current track: {self.__tlist[self.__current_track]}")
    def stop_tracks(self, current_track):
        self.__current_track = current_track
        if self.__tlist and len(self.__tlist) > self.__current_track:
            print(f"stopping current track: {self.__tlist[self.__current_track]}")
    def change_tracks(self, change_track):
        self.__current_track = change_track
        if self.__tlist and len(self.__tlist) > self.__current_track:
            print(f"changing to track: {self.__tlist[self.__current_track]}")
    def retrieve_tracks(self):
        return self.__tlist
# TODO: Remember to explain your OOP design choice in the comments.

# TODO: Create an instance of your MusicPlayer.
music = MusicPlayer()
music.add_tracks("Happy Holiday!")
music.add_tracks("Merry Christmas!!!")
music.play_tracks(0)
music.change_tracks(1)
music.retrieve_tracks()
for track in music.retrieve_tracks():
    print(f"this is {track}")
# TODO: Demonstrate how your music player can add tracks, change to a specific track, then play music, and finally print the list of all tracks.
