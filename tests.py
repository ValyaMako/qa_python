import pytest

from main import BooksCollector

class TestBooksCollector:

    # Тестируем add_new_book - добавление книг в словарь books_genre
    def test_add_new_book_add_two_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Солярис')
        collector.add_new_book('Сияние')
        assert list(collector.books_genre.keys()) == ['Солярис', 'Сияние']

    # Тестируем add_new_book - негативный тест
    @pytest.mark.parametrize('name', ['', 'СияниеСияниеСияниеСияниеСияниеСияниеСияние'])
    def test_add_new_book_add_name_0_symb_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert list(collector.books_genre.keys()) == []

    # Тестируем add_new_book - негативный тест (длина названия 42 символа)
    def test_add_new_book_add_name_42_symb_not_added(self):
            collector = BooksCollector()
            collector.add_new_book('')
            collector.add_new_book('СияниеСияниеСияниеСияниеСияниеСияниеСияние')
            assert list(collector.books_genre.keys()) == []
    # Тестируем add_new_book - негативный тест (добавление книги, которая уже есть в словаре)
    def test_add_new_book_re_adding_books_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert list(collector.books_genre.keys()) == ['Дюна']

    # Тестируем set_book_genre - установление книге жанра
    @pytest.mark.parametrize(
        'name, genre',
    [
        ['Солярис', 'Фантастика'],
        ['Сияние', 'Ужасы'],
        ['Шерлок', 'Детективы'],
        ['Ходячий замок', 'Мультфильмы'],
        ['Эмма', 'Комедии']
    ])
    def test_set_book_genre_genre_set(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre

    # Тестируем set_book_genre - негативный тест (не получиться установить жанр, которого нет в списке self.genre)
    def test_set_book_genre_missing_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Драма')

        assert collector.books_genre['Солярис'] == ''

    # Тестируем get_book_genre - получение жанра книги по её имени
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Солярис', 'Фантастика'],
            ['Сияние', 'Ужасы'],
            ['Шерлок', 'Детективы'],
            ['Ходячий замок', 'Мультфильмы'],
            ['Эмма', 'Комедии']
        ])
    def test_get_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    # Тестируем get_books_with_specific_genre - получение списка книг с определенным жанром
    def test_get_books_with_specific_genre(self, books):
        collector = BooksCollector()
        for keys, values in books.items():
            collector.add_new_book(keys)
            collector.set_book_genre(keys, values)
        assert collector.get_books_with_specific_genre('Фантастика') == ['Солярис', 'Пикник у обочины', 'Дюна']

    # Тестируем get_books_genre - получение словаря
    def test_get_books_genre(self, books):
        collector = BooksCollector()
        for keys, values in books.items():
            collector.add_new_book(keys)
            collector.set_book_genre(keys, values)
        expected_dict = {
            'Солярис': 'Фантастика',
            'Пикник у обочины': 'Фантастика',
            'Дюна': 'Фантастика',
            'Ночная смена': 'Ужасы',
            'Сияние': 'Ужасы',
        }
        assert collector.get_books_genre() == expected_dict

    # Тестируем get_books_for_children - получение списка книг, подходящих для детей
    def test_get_books_for_children(self, books):
        collector = BooksCollector()
        for keys, values in books.items():
            collector.add_new_book(keys)
            collector.set_book_genre(keys, values)
        assert collector.get_books_for_children() == ['Солярис', 'Пикник у обочины', 'Дюна']

    # Тестируем add_book_in_favorites - добавление книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ходячий замок')
        collector.add_book_in_favorites('Ходячий замок')

        assert 'Ходячий замок' in collector.favorites

    # Тестируем delete_book_from_favorites - удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ходячий замок')
        collector.add_book_in_favorites('Ходячий замок')
        collector.delete_book_from_favorites('Ходячий замок')

        assert 'Ходячий замок' not in collector.favorites

    # Тестируем get_list_of_favorites_books - получение списка избранных книг
    def test_get_list_of_favorites_books(self, books):
        collector = BooksCollector()
        for key in books.keys():
            collector.add_new_book(key)
            collector.add_book_in_favorites(key)
        expected_list = ['Солярис', 'Пикник у обочины', 'Дюна', 'Ночная смена', 'Сияние']

        assert collector.get_list_of_favorites_books() == expected_list

