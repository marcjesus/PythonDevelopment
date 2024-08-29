class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title: str):
        # Insert the book title while keeping the list sorted
        self.books.append(title)
        self.books.sort()  # Keep the list sorted

    def search_book(self, title: str) -> bool:
        # Implement binary search to find the book
        left, right = 0, len(self.books) - 1    
        while left <= right:
            mid = (left + right) // 2
            if self.books[mid] == title:
                return True
            elif self.books[mid] < title:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def get_books_starting_with(self, letter: str):
        # Use list comprehension to find books starting with the given letter
        return [book for book in self.books if book.startswith(letter)]

# Example usage:
library = Library()

# Add books to the library
library.add_book("The Catcher in the Rye")
library.add_book("To Kill a Mockingbird")
library.add_book("1984")
library.add_book("The Great Gatsby")

# Search for a book
print(library.search_book("1984"))  # Output: True
print(library.search_book("Moby Dick"))  # Output: False

# Get books starting with 'T'
print(library.get_books_starting_with("T"))  # Output: ['The Catcher in the Rye', 'The Great Gatsby', 'To Kill a Mockingbird']
