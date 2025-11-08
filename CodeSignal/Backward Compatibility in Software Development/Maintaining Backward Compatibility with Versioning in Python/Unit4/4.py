class StandardVideoFormat:
    def __init__(self, frameRate, resolution, content):
        self.frameRate = frameRate
        self.resolution = resolution
        self.content = content  # Assume byte array

# TODO: Implement AdvancedFilterProcessor with a method applyFilter that applies a filter to the video
class AdvancedFilterProcessor:
    # To apply a filter for a video, you can use this kind of transformation:
    # video.content = bytes(filterType + "_" + video.content.decode('utf-8'), 'utf-8')
    #pass
    def applyFilter(self, video, filterType=None):
        if not (filterType == "grayscale" or filterType == "sepia" or filterType == "invert"): 
            return video
        elif filterType == None: return video 
        else: 
            video.content = bytes(filterType + "_" + video.content.decode('utf-8'), 'utf-8')
            return video

# TODO: Implement FilterAdapter class using AdvancedFilterProcessor instance for backward compatibility
class FilterAdapter():
    #pass
    def __init__(self):
        self.advanceFilter = AdvancedFilterProcessor()
    def processVideo(self, video, filterType=None):
        if not (filterType == "grayscale" or filterType == "sepia" or filterType == "invert"): 
            return video
        elif filterType == None: return video 
        else: 
            return self.advanceFilter.applyFilter(video, filterType)

# Example usage (uncomment and modify once TODOs are completed):
video = StandardVideoFormat(24, "1080p", bytes("original_video_content", "utf-8"))
adapter = FilterAdapter()
try:
     filtered_video = adapter.processVideo(video, "grayscale")
     print(filtered_video.content) # expected: grayscale_original_video_content
except NotImplementedError:
     print("Feature not implemented")
