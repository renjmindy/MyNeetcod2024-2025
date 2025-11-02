class BookDetails:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
    def display(self):
        print(f"Book Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"ISBN: {self.__isbn}")
    
class InventoryManagement:
    def __init__(self, quantity, price):
        self.__quantity = quantity
        self.__price = price
    def display(self):
        print(f"Quantity in stock: {self.__quantity}")
    def update_quantity(self, current_quantity):
        self.__quantity = current_quantity
    def calculate_total_value(self):
        return self.__quantity * self.__price

class Book:
    def __init__(self, title, author, isbn, quantity, price):
        self.book = BookDetails(title, author, isbn)
        self.inventory = InventoryManagement(quantity, price)
        
        #self.title = title
        #self.author = author
        #self.isbn = isbn
        #self.quantity = quantity
        #self.price = price
        
    def display_book_information(self):
        print("Book Information:")
        self.book.display()
        self.inventory.display()
        
        #print(f"Book Title: {self.title}")
        #print(f"Author: {self.author}")
        #print(f"ISBN: {self.isbn}")
        #print(f"Quantity in stock: {self.quantity}")
        #print(f"Total Value: ${self.calculate_total_value():.2f}")
    
    def update_quantity(self, current_quantity):
        #self.quantity = quantity
        self.inventory.update_quantity(current_quantity)

    def calculate_total_value(self):
        #return self.quantity * self.price
        self.inventory.calculate_total_value()

# An example of creating and displaying book information using the combined single-class structure
book1 = Book("Refactoring", "Martin Fowler", "978-0201485677", 50, 47.99)
book1.display_book_information()
