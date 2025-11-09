class LibrarySystem:
    def __init__(self):
        self.books = {}
        self.available_books = set()
        self.history = dict()

    def add_book(self, book_id: str, title: str) -> bool:
        if book_id in self.books:
            return False
        self.books[book_id] = {'title': title, 'status': 'available'}
        self.available_books.add(book_id)
        self.history[book_id] = list()
        return True

    def list_books(self) -> list:
        return [self.books[book_id]['title'] for book_id in self.available_books]

    def borrow_book(self, book_id: str) -> bool:
        if book_id not in self.books or book_id not in self.available_books:
            return False
        self.books[book_id]['status'] = 'borrowed'
        self.available_books.remove(book_id)
        self.history[book_id].append('borrowed')
        return True

    def return_book(self, book_id: str) -> bool:
        if book_id not in self.books or self.books[book_id]['status'] == 'available':
            return False
        self.books[book_id]['status'] = 'available'
        self.available_books.add(book_id)
        self.history[book_id].append('returned')
        return True
        
    def reserve_book(self, book_id: str) -> bool:
        for i in range(len(self.history[book_id]) - 1, -1, -1):
            if self.history[book_id][i] == 'reserved' and self.history[book_id][i-1] == 'borrowed': return False
        self.history[book_id].append('reserved')
        return True
        
    def get_book_history(self, book_id: str) -> list[str]:
        return self.history[book_id]
