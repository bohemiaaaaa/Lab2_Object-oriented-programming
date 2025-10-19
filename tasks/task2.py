#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from library_package.library_model import Book, Subscriber


def main():
    subscriber = Subscriber()
    subscriber.read()

    book1 = Book("Толстой Л.Н.", "Война и мир", 1869, "Эксмо", 1500.0)
    book2 = Book("Достоевский Ф.М.", "Преступление и наказание", 1866, "АСТ", 800.0)
    book3 = Book("Пушкин А.С.", "Евгений Онегин", 1833, "Дрофа", 600.0)

    subscriber.add_book(book1, "2024-01-01")
    subscriber.add_book(book2, "2024-12-01")
    subscriber.add_book(book3, "2024-11-15")

    subscriber.display()

    print(f"\nКоличество книг: {len(subscriber)}")
    print(f"Первая книга: {subscriber[0]}")
    print(f"Есть ли книга Толстого: {book1 in subscriber}")

    print("\nКниги Толстого:")
    for book in subscriber.find_by_author("Толстой Л.Н."):
        print(f"  - {book}")

    debt = subscriber.generate_debt()
    print("\nДолг:")
    debt.display()


if __name__ == "__main__":
    main()
