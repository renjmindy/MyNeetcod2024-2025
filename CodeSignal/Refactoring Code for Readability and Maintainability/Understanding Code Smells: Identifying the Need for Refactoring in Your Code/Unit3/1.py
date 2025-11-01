class Book:
    def __init__(self, title, author, isbn, price):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__price = price

    def display_book_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"ISBN: {self.__isbn}")
        print(f"Price: ${self.__price:.2f}")

    def apply_discount(self, discount_percentage):
        #global price
        self.__price *= (1 - discount_percentage / 100)


#title = "Refactoring: Improving the Design of Existing Code"
#author = "Martin Fowler"
#isbn = "978-0134757599"
#price = 47.99

book = Book("Refactoring: Improving the Design of Existing Code", "Martin Fowler", "978-0134757599", 47.99)

# Display the book information
book.display_book_info()
# Apply a 10% discount to the book
book.apply_discount(10)
# Display the book information again to show the updated price
print("After applying discount:")
book.display_book_info()
