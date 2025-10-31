# TODO: You need to define two classes - first, a class named MP3File that supports a 'play' method to print "Playing MP3 file".
class MP3File:
    def play(self):
        print("Playing MP3 file")

# TODO: Second, define another class named WAVFile that also has a play method to print "Playing WAV file".
class WAVFile:
    def play(self):
        print("Playing WAV file")
        
# TODO: Create a list containing instances of MP3File and WAVFile.
rlist = [MP3File(), WAVFile()]

# TODO: Iterate over the list and call the play method on each audio file instance.
for r in rlist:
    r.play()
# Explain the chosen OOP method and your comments below:
# TODO: Add your comments
