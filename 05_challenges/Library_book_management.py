class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__available = True  # Private attribute

    def is_available(self):
        return self.__available

    def check_out(self):
        if self.__available:
            self.__available = False
            print(f"You have checked out '{self.title}'.")
        else:
            print(f"The book '{self.title}' is not available.")

    def return_book(self):
        self.__available = True
        print(f"You have returned '{self.title}'.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title:
                book.check_out()
                return
        print(f"The book '{title}' is not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"The book '{title}' is not found in the library.")

    def display_available_books(self):
        available_books = [book.title for book in self.books if book.is_available()]
        print("Available books:", available_books)

# Example usage:
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

library.display_available_books()

library.check_out_book("The Great Gatsby")
library.display_available_books()

library.return_book("The Great Gatsby")
library.display_available_books()
