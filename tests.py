import pytest
from main import BooksCollector  # Замените на реальное имя модуля с классом

@pytest.fixture
def empty_collector():
    #Фикстура для создания пустого экземпляра BooksCollector
    return BooksCollector()

@pytest.fixture
def collector_with_books(empty_collector):
    #Фикстура для добавления книг в BooksCollector
    empty_collector.add_new_book("Книга1")
    empty_collector.add_new_book("Книга2")
    return empty_collector


class TestBooksCollector:
    @pytest.mark.parametrize("book_name", ["Книга3", "Книга4", "Новая Книга"])
    def test_add_new_book(self, empty_collector, book_name):
        empty_collector.add_new_book(book_name)
        assert book_name in empty_collector.get_books_genre()

    @pytest.mark.parametrize("book_name, genre", [
        ("Книга1", "Фантастика"),
        ("Книга2", "Комедии"),
        ("Книга1", "Детективы")
    ])

    def test_set_book_genre(self, collector_with_books, book_name, genre):
        collector_with_books.set_book_genre(book_name, genre)
        assert collector_with_books.get_book_genre(book_name) == genre

    def test_get_book_genre(self, collector_with_books):
        collector_with_books.set_book_genre("Книга1", "Фантастика")
        assert collector_with_books.get_book_genre("Книга1") == "Фантастика"

    def test_get_books_with_specific_genre(self, collector_with_books):
        collector_with_books.set_book_genre("Книга1", "Фантастика")
        collector_with_books.set_book_genre("Книга2", "Фантастика")
        assert collector_with_books.get_books_with_specific_genre("Фантастика") == ["Книга1", "Книга2"]

    def test_get_books_genre(self, collector_with_books):
        expected_books = {"Книга1": '', "Книга2": ''}
        assert collector_with_books.get_books_genre() == expected_books

    def test_get_books_for_children(self, collector_with_books):
        collector_with_books.set_book_genre("Книга1", "Фантастика")
        collector_with_books.set_book_genre("Книга2", "Ужасы")
        assert collector_with_books.get_books_for_children() == ["Книга1"]

    def test_add_book_in_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites("Книга1")
        assert "Книга1" in collector_with_books.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector_with_books):
        collector_with_books.add_book_in_favorites("Книга1")
        collector_with_books.delete_book_from_favorites("Книга1")
        assert "Книга1" not in collector_with_books.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector_with_books):
        collector_with_books.add_book_in_favorites("Книга1")
        collector_with_books.add_book_in_favorites("Книга2")
        assert collector_with_books.get_list_of_favorites_books() == ["Книга1", "Книга2"]
