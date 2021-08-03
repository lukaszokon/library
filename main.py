import datetime

from library import Library


if __name__ == '__main__':
    library_instance = Library()
    library_instance.add_book('Wiedźmin', 'Andrzej Sapkowski', 'Fantasy', datetime.datetime.fromisoformat('1993-01-01'))
    library_instance.add_book('Diuna', 'Frank Herbert', 'Sci-Fi', datetime.datetime.fromisoformat('1965-01-01'))
    library_instance.print_all_books()
    library_instance.remove_book(id=2)
    library_instance.print_all_books()

