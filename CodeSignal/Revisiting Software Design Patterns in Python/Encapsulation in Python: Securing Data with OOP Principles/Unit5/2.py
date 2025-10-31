# TODO: You should define two classes - an MP3Player class that should have a 'play' method to simulate decoding and playing an MP3 file.
class MP3Player:
    def play(self):
        print("decoding...playing a MP3 file")
class WAVPlayer:
    def __init__(self, file):
        self.file = file
    def play(self):
        print(f"decoding...playing a WAVPlayer {self.file}")
        
mp3 = MP3Player()
wav = WAVPlayer("Marie Carie")
mp3.play()
wav.play()
# TODO: Also, define a second class WAVPlayer that should also have a `play` method to simulate decoding and playing a WAV file.

# TODO: Demonstrate playing files with MP3Player and WAVPlayer by creating instances of both and calling their play methods with a sample file as an argument.

# Explain your choice of OOP principle in the comments below:
# TODO: add your comments
