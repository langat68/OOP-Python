class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                print(f"{self.name} returned {book.title}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            status = "Available" if not book.is_borrowed else "Borrowed"
            print(f"{book.title} by {book.author} - {status}")


# Example usage
library = Library()

book1 = Book("Clean Code", "Robert C. Martin")
book2 = Book("The Pragmatic Programmer", "Andrew Hunt")

library.add_book(book1)
library.add_book(book2)

member1 = Member("Alice")

library.show_books()
print()

member1.borrow_book(book1)
library.show_books()
print()

member1.return_book(book1)
library.show_books()
