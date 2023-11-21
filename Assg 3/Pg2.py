class Author:
    def __init__(self, author_id, name):
        self.author_id = author_id
        self.name = name

    def __str__(self):
        return f"Author ID: {self.author_id}, Name: {self.name}"


class Book:
    def __init__(self, book_id, title, author, num_copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.num_copies = num_copies

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, {str(self.author)}, Copies available: {self.num_copies}"

    def increase_copies(self, num):
        self.num_copies += num

    def decrease_copies(self, num):
        if self.num_copies >= num:
            self.num_copies -= num
        else:
            print("Error: Insufficient copies available.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author_name):
        result = [book for book in self.books if book.author.name == author_name]
        return result

    def search_by_title(self, title):
        result = [book for book in self.books if book.title.lower() == title.lower()]
        return result

    def display_books(self):
        for book in self.books:
            print(book)


# Example usage:
author1 = Author(1, "John Doe")
author2 = Author(2, "Jane Smith")

book1 = Book(101, "Introduction to Python", author1, 5)
book2 = Book(102, "Data Science Basics", author2, 3)
book3 = Book(103, "Advanced Python Programming", author1, 2)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Books by John Doe:")
john_doe_books = library.search_by_author("John Doe")
for book in john_doe_books:
    print(book)

print("\nBooks with 'Python' in the title:")
python_books = library.search_by_title("Python")
for book in python_books:
    print(book)

print("\nAll Books in the Library:")
library.display_books()

# Adding more copies of a book
book1.increase_copies(3)
print(f"\nAfter adding more copies of 'Introduction to Python':\n{book1}")

# Attempting to decrease copies more than available
book2.decrease_copies(5)  # Should display an error message
