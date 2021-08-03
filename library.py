from dataclasses import dataclass, field
from book import Book
import datetime


@dataclass
class Library:
    books: list = field(default_factory=list)
    books_last_id: int = 0

    def add_book(self, title: str, author: str, genre: str, published: datetime):
        self.books_last_id += 1
        new_book = Book(id=self.books_last_id, title=title, author=author, genre=genre, published=published)
        self.books.append(new_book)

    def print_all_books(self):
        for book in self.books:
            print(book)

    def find_book(self, title: str):
        book_instance = None
        for book in self.books:
            if book.title == title:
                book_instance = book
                break
        return book_instance

    def remove_book(self, title: str = None, id: int = None):
        if title:
            book_instance = self.find_book(title)
            if book_instance:
                self.books.remove(book_instance)
                return True
            else:
                return False
        else:
            book_instance = None
            for book in self.books:
                if book.id == id:
                    book_instance = book
                    break
            if book_instance:
                self.books.remove(book_instance)
                return True
            else:
                return False