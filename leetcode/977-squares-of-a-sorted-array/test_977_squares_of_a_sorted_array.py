"""Squares of a Sorted Array

URL: https://leetcode.com/problems/squares-of-a-sorted-array/
"""
from typing import List


class Solution:
    @staticmethod
    def sorted_squares(numbers: List[int]) -> List[int]:
        length = len(numbers)
        result = [0 for _ in range(length)]

        left = 0
        right = len(numbers) - 1
        cursor = right
        while left <= right:
            i_left = abs(numbers[left])
            i_right = abs(numbers[right])

            if i_left >= i_right:
                result[cursor] = i_left ** 2
                left += 1
                cursor -= 1
            else:
                result[cursor] = i_right ** 2
                right -= 1
                cursor -= 1

        return result


def test_case_1():
    numbers = [-4, -1, 0, 3, 10]
    assert Solution.sorted_squares(numbers) == [0, 1, 9, 16, 100]


def test_case_2():
    numbers = [-7, -3, 2, 3, 11]
    assert Solution.sorted_squares(numbers) == [4, 9, 9, 49, 121]


def test_case_3():
    numbers = [-7, -6, 1, 2, 3]
    assert Solution.sorted_squares(numbers) == [1, 4, 9, 36, 49]


def test_case_4():
    numbers = [-7, -6, -5, -3, 3]
    assert Solution.sorted_squares(numbers) == [9, 9, 25, 36, 49]
