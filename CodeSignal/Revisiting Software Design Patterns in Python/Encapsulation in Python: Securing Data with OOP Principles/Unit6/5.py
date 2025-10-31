# Define an interface MediaPlayerInterface with a method play. Remember that this method should not have an implementation within this interface.
class MediaPlayerInterface:
    def play(self):
        pass
# Define a class MediaPlayer, which can aggregate various media files and play them. Remember to implement methods for adding media files and playing all added files.
class MediaPlayer():
    def __init__(self):
        self.mlist = list()
    def add_media(self, media):
        self.mlist.append(media)
    def play(self):
        for m in self.mlist:
            m.play()
# Define classes MP4File and MP3File, both should conform to the MediaPlayerInterface by providing their specific implementation of the play method.
class MP4File(MediaPlayerInterface):
    def play(self):
        print(f"playing mp4")
        
class MP3File(MediaPlayerInterface):
    def play(self):
        print(f"playing mp3")
        
# Instantiate MediaPlayer, create instances of MP4File and MP3File, add these media files to the MediaPlayer's list, and play them.
media_player = MediaPlayer()
mp4_player = MP4File()
mp3_player = MP3File()
media_player.add_media(mp4_player)
media_player.add_media(mp3_player)
media_player.play()

# Examine your design and use of abstraction and composition, and comment on your approach.
