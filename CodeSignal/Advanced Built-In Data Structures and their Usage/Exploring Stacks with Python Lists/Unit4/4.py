from sortedcontainers import SortedDict

# TODO: Define the Book class with a constructor for 'author' and 'title', and implement the logic to sort books by the author's name.
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        
    def __lt__(self, other):
        return (self.author, self.title) < (other.author, other.title)

    def __gt__(self, other):
        return (self.author, self.title) > (other.author, other.title)

    def __eq__(self, other):
        return (self.author, self.title) == (other.author, other.title)

    def __ne__(self, other):
        return (self.author, self.title) != (other.author, other.title)
    
    def __hash__(self):
        return hash((self.author, self.title))

# Initialize the sorted map with books sorted by author's name
library = SortedDict({Book("Orwell", "1984"): 1000, Book("Huxley", "Brave New World"): 2000})

# TODO: Add at least two Book instances to 'library' with different authors and titles. Each book should be mapped to its price (integer).
john = Book("John", "Happy Chinese New Year")
alice = Book("Alice", "Happy Thanksgiving")
library[john] = 1200
library[alice] = 2500

# TODO: Write a loop to print all books in 'library', displaying each book's title and author.
for book in library:
    print(f"title: {book.title}, author: {book.author}, {library[book]}")
