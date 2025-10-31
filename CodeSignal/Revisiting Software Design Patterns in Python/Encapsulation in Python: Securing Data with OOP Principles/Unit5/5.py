class TextEditor:
    def write(self):
        pass

class CodeEditor(TextEditor):
    def write(self):
        print("Writing code...")

class ProseEditor(TextEditor):
    def write(self):
        print("Writing prose...")

# TODO: Your task is to implement an EditorSuite class that can aggregate various editors and has methods to add editors (`add_editor`) and publish writings (`publish`)
class EditorSuite:
    def __init__(self):
        self.elist = list()
# `add_editor(editor)` adds the provided editor for tracking
    def add_editor(self, editor):
        self.elist.append(editor)
# `publish()` prints each tracked editor's writing
    def publish(self):
        for e in self.elist:
            e.write()

# Instantiate EditorSuite, add instances of CodeEditor and ProseEditor to it
# Call publish method of EditorSuite to demonstrate it works as expected
editor = EditorSuite()
editor.add_editor(CodeEditor())
editor.add_editor(ProseEditor())
editor.publish()

# Explain your approach and choice of OOP principle in the comments
# TODO: add your comments here
