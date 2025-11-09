class LibraryManagementSystem:
    def __init__(self):
        self.books = {}
        self.borrow_status = {}
        self.borrow_history = {}
        self.reservation_status = {}

    def add_book(self, book_id: str, title: str) -> bool:
        if book_id not in self.books:
            self.books[book_id] = title
            self.borrow_status[book_id] = False
            return True
        return False

    def check_availability(self, book_id: str) -> str | None:
        if book_id in self.books and not self.borrow_status[book_id]:
            return self.books[book_id]
        return None

    def borrow_book(self, user_id: str, book_id: str) -> bool:
        if book_id in self.books and not self.borrow_status[book_id]:
            self.borrow_status[book_id] = True
            if book_id not in self.borrow_history:
                self.borrow_history[book_id] = []
            self.borrow_history[book_id].append(user_id)
            return True
        return False

    def return_book(self, book_id: str) -> bool:
        if book_id in self.books and self.borrow_status[book_id]:
            self.borrow_status[book_id] = False
            if self.reservation_status.get(book_id, []): 
                self.borrow_book(self.reservation_status[book_id][0], book_id)
                self.reservation_status[book_id].pop(0)
            return True
        return False

    def get_borrow_history(self, book_id: str) -> list[str]:
        if book_id in self.borrow_history:
            return self.borrow_history[book_id]
        return []
        
    def reserve_book(self, user_id: str, book_id: str) -> bool:
        if book_id in self.books and self.borrow_status[book_id] == False: 
            return False
        if book_id not in self.reservation_status: self.reservation_status.setdefault(book_id, [])
        if user_id not in self.reservation_status[book_id]:
            self.reservation_status.setdefault(book_id, []).append(user_id)
        return True
        
    def notify_availability(self, book_id: str) -> str:
        if book_id in self.books and self.borrow_status[book_id] == False: 
            return self.reservation_status[book_id][0]
        else: None
        
    def check_reservation(self, book_id: str) -> str:
        if self.reservation_status.get(book_id, []): return self.reservation_status[book_id][0]
        else: None
        
