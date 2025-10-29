from sortedcontainers import SortedDict

class Book:
    def __init__(self, title, publication_year):
        self.title = title
        self.publication_year = publication_year

library = SortedDict()
library[2021] = Book("Python 101", 2021)
# TODO: Add another book to the library with the publication year as the key, remember the book's uniqueness comes from its title and year.
library[2022] = Book("Python 102", 2022)
# TODO: Iterate through library and print the book title and its publication year.
for year in library:
    print(f"title: {library[year].title}, year: {library[year].publication_year}")
