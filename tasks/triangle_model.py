#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt


class RightTrianglePair:
    def __init__(self, first: float = 1, second: float = 1) -> None:
        self.first = first
        self.second = second

    @property
    def first(self) -> float:
        return self.__first

    @first.setter
    def first(self, value: float) -> None:
        value = float(value)
        if value <= 0:
            raise ValueError("Катеты должны быть положительными числами")
        self.__first = value

    @property
    def second(self) -> float:
        return self.__second

    @second.setter
    def second(self, value: float) -> None:
        value = float(value)
        if value <= 0:
            raise ValueError("Катеты должны быть положительными числами")
        self.__second = value

    def read(self) -> None:
        self.first = float(input("Введите первый катет: "))
        self.second = float(input("Введите второй катет: "))

    def display(self) -> None:
        print(f"Первый катет: {self.first}")
        print(f"Второй катет: {self.second}")
        print(f"Гипотенуза: {self.hypotenuse:.2f}")

    @property
    def hypotenuse(self) -> float:
        return sqrt(self.first**2 + self.second**2)

    def __str__(self) -> str:
        return (
            f"RightTrianglePair({self.first:.0f}, {self.second:.0f})"
            if self.first.is_integer() and self.second.is_integer()
            else f"RightTrianglePair({self.first}, {self.second})"
        )

    def __repr__(self) -> str:
        first = int(self.first) if self.first.is_integer() else self.first
        second = int(self.second) if self.second.is_integer() else self.second
        return f"RightTrianglePair({first}, {second})"

    def __eq__(self, other) -> bool:
        if isinstance(other, RightTrianglePair):
            return self.first == other.first and self.second == other.second
        return False

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        if isinstance(other, RightTrianglePair):
            return self.hypotenuse < other.hypotenuse
        return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, RightTrianglePair):
            return self.hypotenuse <= other.hypotenuse
        return NotImplemented

    def __gt__(self, other) -> bool:
        if isinstance(other, RightTrianglePair):
            return self.hypotenuse > other.hypotenuse
        return NotImplemented

    def __ge__(self, other) -> bool:
        if isinstance(other, RightTrianglePair):
            return self.hypotenuse >= other.hypotenuse
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RightTrianglePair):
            return RightTrianglePair(
                self.first + other.first, self.second + other.second
            )
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RightTrianglePair):
            return RightTrianglePair(
                max(0.1, self.first - other.first), max(0.1, self.second - other.second)
            )
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return RightTrianglePair(self.first * other, self.second * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Деление на ноль")
            return RightTrianglePair(self.first / other, self.second / other)
        return NotImplemented

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return RightTrianglePair(
                max(0.1, other - self.first), max(0.1, other - self.second)
            )
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __iadd__(self, other):
        if isinstance(other, RightTrianglePair):
            self.first += other.first
            self.second += other.second
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, RightTrianglePair):
            self.first = max(0.1, self.first - other.first)
            self.second = max(0.1, self.second - other.second)
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.first *= other
            self.second *= other
            return self
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ValueError("Деление на ноль")
            self.first /= other
            self.second /= other
            return self
        return NotImplemented

    def __float__(self) -> float:
        return self.hypotenuse

    def __int__(self) -> int:
        return int(self.hypotenuse)

    def __bool__(self) -> bool:
        return self.first > 0 and self.second > 0

    def __call__(self) -> float:
        return self.hypotenuse

    def __getitem__(self, index):
        if index == 0:
            return self.first
        elif index == 1:
            return self.second
        elif index == 2:
            return self.hypotenuse
        raise IndexError("Index must be 0, 1 or 2")

    def __len__(self):
        return 3

    def __contains__(self, item):
        return item in [self.first, self.second, self.hypotenuse]

    def __iter__(self):
        return iter([self.first, self.second, self.hypotenuse])


def make_right_triangle_pair(first: float, second: float) -> RightTrianglePair:
    return RightTrianglePair(first, second)
