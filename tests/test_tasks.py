#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

import pytest
from library_package.library_model import Book, BorrowedBook, Debt, Subscriber
from triangle_model import RightTrianglePair, make_right_triangle_pair


class TestRightTrianglePair:
    def test_creation_default(self):
        triangle = RightTrianglePair()
        assert triangle.first == 1
        assert triangle.second == 1

    def test_creation_with_values(self):
        triangle = RightTrianglePair(3, 4)
        assert triangle.first == 3
        assert triangle.second == 4

    def test_hypotenuse_calculation(self):
        triangle = RightTrianglePair(3, 4)
        assert triangle.hypotenuse == 5.0

    def test_negative_first_cathetus(self):
        with pytest.raises(
            ValueError, match="Катеты должны быть положительными числами"
        ):
            RightTrianglePair(-1, 4)

    def test_negative_second_cathetus(self):
        with pytest.raises(
            ValueError, match="Катеты должны быть положительными числами"
        ):
            RightTrianglePair(3, -1)

    def test_zero_cathetus(self):
        with pytest.raises(
            ValueError, match="Катеты должны быть положительными числами"
        ):
            RightTrianglePair(0, 4)

    def test_equality(self):
        t1 = RightTrianglePair(3, 4)
        t2 = RightTrianglePair(3, 4)
        assert t1 == t2

    def test_inequality(self):
        t1 = RightTrianglePair(3, 4)
        t2 = RightTrianglePair(5, 12)
        assert t1 != t2

    def test_less_than(self):
        t1 = RightTrianglePair(3, 4)  # гипотенуза = 5
        t2 = RightTrianglePair(5, 12)  # гипотенуза = 13
        assert t1 < t2

    def test_greater_than(self):
        t1 = RightTrianglePair(5, 12)  # гипотенуза = 13
        t2 = RightTrianglePair(3, 4)  # гипотенуза = 5
        assert t1 > t2

    def test_addition(self):
        t1 = RightTrianglePair(3, 4)
        t2 = RightTrianglePair(1, 2)
        result = t1 + t2
        assert result.first == 4
        assert result.second == 6

    def test_subtraction(self):
        t1 = RightTrianglePair(5, 6)
        t2 = RightTrianglePair(1, 2)
        result = t1 - t2
        assert result.first == 4
        assert result.second == 4

    def test_multiplication(self):
        t1 = RightTrianglePair(3, 4)
        result = t1 * 2
        assert result.first == 6
        assert result.second == 8

    def test_division(self):
        t1 = RightTrianglePair(6, 8)
        result = t1 / 2
        assert result.first == 3
        assert result.second == 4

    def test_division_by_zero(self):
        t1 = RightTrianglePair(3, 4)
        with pytest.raises(ValueError, match="Деление на ноль"):
            t1 / 0

    def test_float_conversion(self):
        t1 = RightTrianglePair(3, 4)
        assert float(t1) == 5.0

    def test_int_conversion(self):
        t1 = RightTrianglePair(3, 4)
        assert int(t1) == 5

    def test_bool_conversion(self):
        t1 = RightTrianglePair(3, 4)
        assert bool(t1) is True

    def test_call(self):
        t1 = RightTrianglePair(3, 4)
        assert t1() == 5.0

    def test_getitem(self):
        t1 = RightTrianglePair(3, 4)
        assert t1[0] == 3
        assert t1[1] == 4
        assert t1[2] == 5.0

    def test_getitem_invalid_index(self):
        t1 = RightTrianglePair(3, 4)
        with pytest.raises(IndexError, match="Index must be 0, 1 or 2"):
            t1[5]

    def test_len(self):
        t1 = RightTrianglePair(3, 4)
        assert len(t1) == 3

    def test_contains(self):
        t1 = RightTrianglePair(3, 4)
        assert 3 in t1
        assert 4 in t1
        assert 5.0 in t1
        assert 10 not in t1

    def test_iteration(self):
        t1 = RightTrianglePair(3, 4)
        values = list(t1)
        assert values == [3, 4, 5.0]

    def test_string_representation(self):
        t1 = RightTrianglePair(3, 4)
        assert str(t1) == "RightTrianglePair(3, 4)"
        assert repr(t1) == "RightTrianglePair(3, 4)"

    def test_inplace_addition(self):
        t1 = RightTrianglePair(3, 4)
        t2 = RightTrianglePair(1, 2)
        t1 += t2
        assert t1.first == 4
        assert t1.second == 6

    def test_inplace_multiplication(self):
        t1 = RightTrianglePair(3, 4)
        t1 *= 2
        assert t1.first == 6
        assert t1.second == 8


class TestMakeRightTrianglePair:
    def test_make_function(self):
        triangle = make_right_triangle_pair(3, 4)
        assert isinstance(triangle, RightTrianglePair)
        assert triangle.first == 3
        assert triangle.second == 4

    def test_make_function_invalid(self):
        with pytest.raises(
            ValueError, match="Катеты должны быть положительными числами"
        ):
            make_right_triangle_pair(-1, 4)


class TestLibraryModel:
    def test_book_creation(self):
        book = Book("Толстой", "Война и мир", 1869, "Эксмо", 1500.0)
        assert book.author == "Толстой"
        assert book.title == "Война и мир"
        assert book.year == 1869
        assert book.publisher == "Эксмо"
        assert book.price == 1500.0

    def test_book_negative_year(self):
        with pytest.raises(ValueError, match="Год издания не может быть отрицательным"):
            Book("Автор", "Книга", -1, "Издательство", 100.0)

    def test_book_negative_price(self):
        with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
            Book("Автор", "Книга", 2024, "Издательство", -100.0)

    def test_book_equality(self):
        book1 = Book("Автор", "Книга", 2024, "Издательство", 100.0)
        book2 = Book("Автор", "Книга", 2024, "Издательство", 100.0)
        book3 = Book("Другой", "Книга", 2024, "Издательство", 100.0)

        assert book1 == book2
        assert book1 != book3

    def test_subscriber_creation(self):
        subscriber = Subscriber("Иванов", "LIB001", 50)

        assert subscriber.name == "Иванов"
        assert subscriber.library_id == "LIB001"
        assert subscriber.size == 50
        assert subscriber.count == 0

    def test_subscriber_size_method(self):
        subscriber = Subscriber("Иванов", "LIB001", 50)
        assert subscriber.get_size() == 50

    def test_subscriber_add_book(self):
        subscriber = Subscriber("Иванов", "LIB001", 5)
        book = Book("Автор", "Книга", 2024, "Издательство", 100.0)

        subscriber.add_book(book)
        assert len(subscriber) == 1
        assert subscriber.count == 1
        assert book in subscriber

    def test_subscriber_add_book_limit(self):
        subscriber = Subscriber("Иванов", "LIB001", 2)
        book1 = Book("Автор1", "Книга1", 2024, "Издательство", 100.0)
        book2 = Book("Автор2", "Книга2", 2024, "Издательство", 100.0)
        book3 = Book("Автор3", "Книга3", 2024, "Издательство", 100.0)

        subscriber.add_book(book1)
        subscriber.add_book(book2)

        with pytest.raises(ValueError, match="Достигнут лимит книг: 2"):
            subscriber.add_book(book3)

    def test_subscriber_remove_book(self):
        subscriber = Subscriber("Иванов", "LIB001", 5)
        book = Book("Автор", "Книга", 2024, "Издательство", 100.0)

        subscriber.add_book(book)
        assert len(subscriber) == 1

        subscriber.remove_book(book)
        assert len(subscriber) == 0
        assert subscriber.count == 0

    def test_subscriber_getitem(self):
        subscriber = Subscriber("Иванов", "LIB001", 5)
        book = Book("Автор", "Книга", 2024, "Издательство", 100.0)

        subscriber.add_book(book)
        assert subscriber[0].book == book

    def test_subscriber_getitem_invalid_index(self):
        subscriber = Subscriber("Иванов", "LIB001", 5)

        with pytest.raises(IndexError, match="Индекс вне диапазона"):
            _ = subscriber[10]

    def test_subscriber_setitem(self):
        subscriber = Subscriber("Иванов", "LIB001", 5)
        book1 = Book("Автор1", "Книга1", 2024, "Издательство", 100.0)
        book2 = Book("Автор2", "Книга2", 2024, "Издательство", 200.0)

        subscriber.add_book(book1)
        borrowed = subscriber[0]
        borrowed.book = book2
        subscriber[0] = borrowed

        assert subscriber[0].book == book2

    def test_subscriber_find_by_author(self):
        subscriber = Subscriber("Иванов", "LIB001", 5)
        book1 = Book("Толстой", "Книга1", 2024, "Издательство", 100.0)
        book2 = Book("Пушкин", "Книга2", 2024, "Издательство", 200.0)
        book3 = Book("Толстой", "Книга3", 2024, "Издательство", 300.0)

        subscriber.add_book(book1)
        subscriber.add_book(book2)
        subscriber.add_book(book3)

        result = subscriber.find_by_author("Толстой")
        assert len(result) == 2
        assert all(borrowed.book.author == "Толстой" for borrowed in result)

    def test_subscriber_calculate_debt_cost(self):
        subscriber = Subscriber("Иванов", "LIB001", 5)
        book1 = Book("Автор1", "Книга1", 2024, "Издательство", 100.0)
        book2 = Book("Автор2", "Книга2", 2024, "Издательство", 200.0)

        old_date = (datetime.now() - timedelta(days=40)).strftime("%Y-%m-%d")
        subscriber.add_book(book1, old_date)
        subscriber.add_book(book2, old_date)

        assert subscriber.calculate_debt_cost() == 300.0

    def test_subscriber_generate_debt(self):
        subscriber = Subscriber("Иванов", "LIB001", 5)
        book = Book("Автор", "Книга", 2024, "Издательство", 100.0)

        old_date = (datetime.now() - timedelta(days=40)).strftime("%Y-%m-%d")
        subscriber.add_book(book, old_date)

        debt = subscriber.generate_debt()
        assert isinstance(debt, Debt)
        assert debt.total_cost == 100.0

    def test_subscriber_addition_same_subscriber(self):
        sub1 = Subscriber("Иванов", "LIB001", 10)
        sub2 = Subscriber("Иванов", "LIB001", 15)

        book1 = Book("Автор1", "Книга1", 2024, "Издательство", 100.0)
        book2 = Book("Автор2", "Книга2", 2024, "Издательство", 200.0)

        sub1.add_book(book1)
        sub2.add_book(book2)

        result = sub1 + sub2
        assert len(result) == 2
        assert result.size == 15

    def test_subscriber_addition_different_subscriber(self):
        sub1 = Subscriber("Иванов", "LIB001", 10)
        sub2 = Subscriber("Петров", "LIB002", 10)

        with pytest.raises(
            ValueError, match="Можно объединять только карточки одного абонента"
        ):
            _ = sub1 + sub2

    def test_subscriber_intersection(self):
        sub1 = Subscriber("Иванов", "LIB001", 10)
        sub2 = Subscriber("Петров", "LIB002", 10)

        book1 = Book("Автор1", "Книга1", 2024, "Издательство", 100.0)
        book2 = Book("Автор2", "Книга2", 2024, "Издательство", 200.0)

        sub1.add_book(book1)
        sub1.add_book(book2)
        sub2.add_book(book1)

        result = sub1 & sub2
        assert len(result) == 1
        assert result[0].book == book1

    def test_subscriber_subtraction(self):
        sub1 = Subscriber("Иванов", "LIB001", 10)
        sub2 = Subscriber("Петров", "LIB002", 10)

        book1 = Book("Автор1", "Книга1", 2024, "Издательство", 100.0)
        book2 = Book("Автор2", "Книга2", 2024, "Издательство", 200.0)

        sub1.add_book(book1)
        sub1.add_book(book2)
        sub2.add_book(book1)

        result = sub1 - sub2
        assert len(result) == 1
        assert result[0].book == book2

    def test_debt_creation(self):
        book = Book("Автор", "Книга", 2024, "Издательство", 100.0)
        borrowed = BorrowedBook(book, "2024-01-01")

        debt = Debt("Иванов", "LIB001", [borrowed])

        assert debt.subscriber_name == "Иванов"
        assert debt.library_id == "LIB001"
        assert len(debt.overdue_books) == 1
        assert debt.total_cost == 100.0
