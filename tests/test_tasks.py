#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
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
