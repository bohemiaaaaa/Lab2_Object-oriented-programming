#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from triangle_model import RightTrianglePair

if __name__ == "__main__":
    triangle = RightTrianglePair()
    triangle.edit()

    print("\nИнформация о треугольнике:")
    print(triangle)

    print("\nИспользование перегруженных операторов:")
    print(f"str(triangle): {triangle}")
    print(f"float(triangle): {float(triangle):.2f}")
    print(f"int(triangle): {int(triangle)}")
    print(f"bool(triangle): {bool(triangle)}")
    print(f"triangle[0]: {triangle[0]}")
    print(f"triangle[1]: {triangle[1]}")
    print(f"triangle[2]: {triangle[2]:.2f}")
    print(f"len(triangle): {len(triangle)}")
    print(f"3.0 in triangle: {3.0 in triangle}")

    t2 = RightTrianglePair(3, 4)
    print(f"\nСравнение с (3,4): {triangle == t2}")
    print(f"triangle < t2: {triangle < t2}")
    print(f"triangle > t2: {triangle > t2}")

    sum_t = triangle + t2
    print(f"Сумма: {sum_t}")

    mul_t = triangle * 2
    print(f"Умножение на 2: {mul_t}")

    triangle += t2
    print(f"После +=: {triangle}")
