class MediaPlayer:
    def play(self, file_type):
        # TODO: Complete the play method to output a message based on the file_type
        # The file_type is either "audio" or "video"
        #pass
        print(f"Playing {file_type} track")

class Speaker:
    def output_sound(self):
        print("Outputting sound")

class Screen:
    def display_image(self):
        print("Displaying image")

class HomeTheater:
    def __init__(self):
        # TODO: initialize composition pattern parts
        #pass
        self.media = MediaPlayer()
        self.speaker = Speaker()
        self.screen = Screen()
        
    def play_media(self, file_type):
        # TODO: Call the appropriate methods to simulate playing media. Consider the file_type.
        # The file_type is either "audio" or "video"
        #pass
        self.media.play(file_type)
        if file_type == 'audio': self.speaker.output_sound()
        if file_type == 'video': self.speaker.output_sound(); self.screen.display_image()

home_theater_system = HomeTheater()
home_theater_system.play_media("video")
