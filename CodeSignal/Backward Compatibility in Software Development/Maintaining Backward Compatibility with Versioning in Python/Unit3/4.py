class AudioFile:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def display_info(self):
        return f"Audio: {self.name}, duration: {self.duration} mins"

# TODO: Add support for Video and Image files in the library using polymorphism
class VideoFile:
    def __init__(self, name, duration, resolution):
        self.name = name
        self.resolution = resolution
        self.duration = duration

    def display_info(self):
        return f"Video: {self.name}, duration: {self.duration} mins, resolution: {self.resolution}"
            
class ImageFile:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def display_info(self):
        return f"Image: {self.name}, dimensions: {self.width}x{self.height}"
            
class MediaLibrary:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_library(self):
        for item in self.items:
            item.display_info()
