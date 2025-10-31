# TODO: Define a class Printer with a method print_document that prints a document
class Printer:
    def print_document(self):
        return "print a document"
# TODO: Define a subclass of Printer named PhotoPrinter which overrides the print_document method for photos
class PhotoPrinter(Printer):
    def print_document(self):
        return "print photos"
# Create instances of both printers and store them in a list. Then, iterate through the list and call the print_document method for each, determining the document type based on the printer type.
objects = [Printer(), PhotoPrinter()]

for object in objects:
    print(object.print_document())
