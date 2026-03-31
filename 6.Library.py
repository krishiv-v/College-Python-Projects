class library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print(f"'{self.book_name}' by {self.author} has been checked out.")
        else:
            print(f"Sorry, '{self.book_name}' is currently not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"'{self.book_name}' has been returned and is now available.")
        else:
            print(f"'{self.book_name}' was not checked out.")

    def display_info(self):
        status = "Available" if self.available else "Checked Out"
        print(f"Book: {self.book_name}, Author: {self.author}, Status: {status}")

book1 = library("Godan", "Premchand")
book2 = library("Gitanjali", "Rabindranath Tagore", available=False)

book1.display_info()
book2.display_info()

book1.check_out()
book1.display_info()

book1.return_book()
book1.display_info()
