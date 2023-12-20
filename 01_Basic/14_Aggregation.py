class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        # Here, the 'author' parameter is an instance of the Author class
        self.author = author

# Creating an Author instance
author1 = Author("Jane Doe")

# Creating a Book instance and passing the Author instance through aggregation
book1 = Book("Sample Book", author1)

# Accessing book information
print(f"Book Title: {book1.title}")
print(f"Author: {book1.author.name}")

#Output : Book Title :  Sample Book
#Outpu2 : Author : Jane Doe
