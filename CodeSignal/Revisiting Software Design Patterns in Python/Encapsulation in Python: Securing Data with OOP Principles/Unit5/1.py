# TODO: Define a Document class with an initializer that initializes an empty string for document content.
class Document:
    def __init__(self):
        self.__doc = ""
    def add_content(self, content):
        self.__doc += content
    def display_content(self):
        print(self.__doc)
    
document = Document()
document.add_content("I am beautiful.")
document.display_content()
# TODO: Add a method to the Document class that lets you append new content (a string) to the document. Remember, external access to the document content should be restricted.

# TODO: Add another method to display all the content of the document beautifully.

# Create an instance of the Document class.

# TODO: Use the methods you've defined to add some content to your document instance.

# TODO: Call the method that displays the document's content.

# Explain your choice of OOP principle in the comments:
# TODO: add your explanation here
