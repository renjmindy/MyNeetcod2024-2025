class MediaPlayer:
    def play(self, file):
        if file.lower().endswith('.mp3'):
            print(f"Playing .mp3 file: {file}")
        else:
            print("Unsupported file format")

# TODO: Implement the AdvancedMediaPlayer class that inherits from MediaPlayer
# It should override the play method to support playing .wav files in addition to the .mp3 files
class AdvancedMediaPlayer(MediaPlayer):
    def play(self, file):
        if file.lower().endswith('.wav'):
            print(f"Playing .wav file: {file}")
        elif file.lower().endswith('.mp3'):
            print(f"Playing .mp3 file: {file}")
        else:
            print("Unsupported file format")
