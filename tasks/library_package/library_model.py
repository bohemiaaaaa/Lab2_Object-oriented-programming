#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta


class Book:
    def __init__(
        self,
        author: str = "",
        title: str = "",
        year: int = 0,
        publisher: str = "",
        price: float = 0.0,
    ) -> None:
        if year < 0:
            raise ValueError("Год издания не может быть отрицательным")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")

        self.author: str = author
        self.title: str = title
        self.year: int = year
        self.publisher: str = publisher
        self.price: float = price

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return (
                self.author == other.author
                and self.title == other.title
                and self.year == other.year
                and self.publisher == other.publisher
                and self.price == other.price
            )
        return False

    def __hash__(self) -> int:
        return hash((self.author, self.title, self.year, self.publisher, self.price))


class BorrowedBook:
    MAX_DAYS = 30

    def __init__(self, book: Book, issue_date: str = "") -> None:
        self.book: Book = book
        self.issue_date: str = issue_date or datetime.now().strftime("%Y-%m-%d")
        self.return_date: str = self._calculate_return_date()
        self.returned: bool = False

    def _calculate_return_date(self) -> str:
        issue_dt = datetime.strptime(self.issue_date, "%Y-%m-%d")
        return_dt = issue_dt + timedelta(days=self.MAX_DAYS)
        return return_dt.strftime("%Y-%m-%d")

    def mark_returned(self) -> None:
        self.returned = True

    def is_overdue(self) -> bool:
        if self.returned:
            return False
        current_date = datetime.now().strftime("%Y-%m-%d")
        return current_date > self.return_date

    def __str__(self) -> str:
        status = "возвращена" if self.returned else "не возвращена"
        overdue = " (просрочена)" if self.is_overdue() else ""
        return (
            f"{self.book} - выдана: {self.issue_date}, "
            f"вернуть до: {self.return_date} [{status}]{overdue}"
        )


class Subscriber:
    MAX_SIZE = 100

    def __init__(
        self, name: str = "", library_id: str = "", size: int = MAX_SIZE
    ) -> None:
        self.name: str = name
        self.library_id: str = library_id
        self.size: int = size
        self.count: int = 0
        self._books: list[BorrowedBook] = []

    def edit(self) -> None:
        """Редактирование данных абонента через консоль"""
        self.name = input("Введите фамилию абонента: ")
        self.library_id = input("Введите библиотечный номер: ")

    def get_size(self) -> int:
        return self.size

    def __str__(self) -> str:
        result = [
            f"Абонент: {self.name}",
            f"Библиотечный номер: {self.library_id}",
            f"Книг на руках: {self.count}/{self.size}",
            "Список книг:",
        ]
        for i, book in enumerate(self._books, 1):
            result.append(f"  {i}. {book}")
        return "\n".join(result)

    def __repr__(self) -> str:
        return f"Subscriber('{self.name}', '{self.library_id}', {self.size})"

    def __getitem__(self, index: int) -> BorrowedBook:
        if 0 <= index < len(self._books):
            return self._books[index]
        raise IndexError("Индекс вне диапазона")

    def __setitem__(self, index: int, value: BorrowedBook) -> None:
        if 0 <= index < len(self._books):
            if self._books[index] != value:
                self._books[index] = value
        else:
            raise IndexError("Индекс вне диапазона")

    def __len__(self) -> int:
        return len(self._books)

    def __contains__(self, book: Book) -> bool:
        return any(borrowed_book.book == book for borrowed_book in self._books)

    def __add__(self, other) -> "Subscriber":
        if not isinstance(other, Subscriber):
            return None

        if self.library_id != other.library_id:
            raise ValueError("Можно объединять только карточки одного абонента")

        new_size = max(self.size, other.size)
        result = Subscriber(self.name, self.library_id, new_size)
        result._books = self._books.copy()
        result.count = self.count

        for book in other._books:
            if book not in result._books and result.count < result.size:
                result._books.append(book)
                result.count += 1

        return result

    def __and__(self, other) -> "Subscriber":
        if not isinstance(other, Subscriber):
            return None

        result = Subscriber(
            f"{self.name} & {other.name}", "intersection", self.MAX_SIZE
        )
        for book in self._books:
            if (
                any(book.book == other_book.book for other_book in other._books)
                and result.count < result.size
            ):
                result._books.append(book)
                result.count += 1
        return result

    def __sub__(self, other) -> "Subscriber":
        if not isinstance(other, Subscriber):
            return None

        result = Subscriber(self.name, self.library_id, self.size)
        for book in self._books:
            if (
                not any(book.book == other_book.book for other_book in other._books)
                and result.count < result.size
            ):
                result._books.append(book)
                result.count += 1
        return result

    def add_book(self, book: Book, issue_date: str = "") -> None:
        if self.count >= self.size:
            raise ValueError(f"Достигнут лимит книг: {self.size}")

        borrowed_book = BorrowedBook(book, issue_date)
        self._books.append(borrowed_book)
        self.count += 1

    def remove_book(self, book: Book) -> None:
        for i, borrowed_book in enumerate(self._books):
            if borrowed_book.book == book:
                self._books.pop(i)
                self.count -= 1
                return
        raise ValueError("Книга не найдена в списке")

    def find_overdue_books(self) -> list[BorrowedBook]:
        return [book for book in self._books if book.is_overdue() and not book.returned]

    def find_by_author(self, author: str) -> list[BorrowedBook]:
        return [
            book for book in self._books if book.book.author.lower() == author.lower()
        ]

    def find_by_publisher(self, publisher: str) -> list[BorrowedBook]:
        return [
            book
            for book in self._books
            if book.book.publisher.lower() == publisher.lower()
        ]

    def find_by_year(self, year: int) -> list[BorrowedBook]:
        return [book for book in self._books if book.book.year == year]

    def calculate_debt_cost(self) -> float:
        overdue_books = self.find_overdue_books()
        return sum(book.book.price for book in overdue_books)

    def generate_debt(self) -> "Debt":
        overdue_books = self.find_overdue_books()
        return Debt(self.name, self.library_id, overdue_books)


class Debt:
    def __init__(
        self, subscriber_name: str, library_id: str, overdue_books: list[BorrowedBook]
    ) -> None:
        self.subscriber_name: str = subscriber_name
        self.library_id: str = library_id
        self.overdue_books: list[BorrowedBook] = overdue_books
        self.total_cost: float = sum(book.book.price for book in overdue_books)

    def __str__(self) -> str:
        result = [
            f"Долг абонента: {self.subscriber_name} ({self.library_id})",
            f"Общая стоимость долга: {self.total_cost:.2f}",
            "Просроченные книги:",
        ]
        for i, book in enumerate(self.overdue_books, 1):
            result.append(f"  {i}. {book}")
        return "\n".join(result)
