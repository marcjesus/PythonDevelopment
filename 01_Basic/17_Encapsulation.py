# Encapsulation describes the act of combining data with the matching methods into a single entity.

class Library:
    def __init__(self, id, name):
        self.bookId = id
        self.bookName = name

    def setBookName(self, newBookName):
        self.bookName = newBookName

    def getBookName(self):
        print(f"The name of book is {self.bookName}")

book = Library(101,"Python beginner")
book.getBookName()
book.setBookName("Python intermediate")
book.getBookName()
