class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})'


class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

if __name__ == '__main__':
    # Инициализируем пустую библиотеку
    empty_library = Library()
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    # Создаем список книг из базы данных
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]

    # Инициализируем библиотеку с книгами
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    # Проверяем индекс книги с id = 1
    print(library_with_books.get_index_by_book_id(1))
