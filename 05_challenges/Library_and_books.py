class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f'Book("{self.title}", "{self.author}", {self.year})'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)

    def get_books_by_author(self, author):
        """Returns a list of titles by the specified author."""
        # Use list comprehension to filter books by author
        return [book.title for book in self.books if book.author == author]

    def get_books_before(self, year):
        """Returns a list of books published before the specified year."""
        # Use list comprehension to filter books by year
        return [book for book in self.books if book.year < year]

    def parse_books(self, data):
        """Parses a list of strings and adds the corresponding Book objects to the library."""
        for entry in data:
            # Split the string by ';' and parse the book details
            title, author, year = entry.split(';')
            self.add_book(Book(title, author, int(year)))

# Example test
library = Library()

book_data = [
    "The Hobbit;J.R.R. Tolkien;1937",
    "1984;George Orwell;1949",
    "To Kill a Mockingbird;Harper Lee;1960"
]
library.parse_books(book_data)
library.add_book(Book("Fahrenheit 451", "Ray Bradbury", 1953))

print(library.get_books_by_author("George Orwell"))  # Output: ['1984']
print(library.get_books_before(1950))  
# Output: [Book("The Hobbit", "J.R.R. Tolkien", 1937), Book("1984", "George Orwell", 1949)]
