"""Move Zeroes

URL: https://leetcode.com/problems/move-zeroes/
"""
from typing import List


class Solution:
    @staticmethod
    def move_zeroes(numbers: List[int]) -> None:
        length = len(numbers)
        non_zero_position = 0
        for index in range(length):
            if numbers[index] != 0:
                numbers[non_zero_position] = numbers[index]
                if non_zero_position != index:
                    numbers[index] = 0
                non_zero_position += 1


def test_case_0():
    numbers = [0, 1, 0, 3, 12]
    Solution.move_zeroes(numbers)
    assert numbers == [1, 3, 12, 0, 0]


def test_case_1():
    numbers = [0]
    Solution.move_zeroes(numbers)
    assert numbers == [0]


def test_case_2():
    numbers = [1]
    Solution.move_zeroes(numbers)
    assert numbers == [1]


def test_case_3():
    numbers = [2, 1]
    Solution.move_zeroes(numbers)
    assert numbers == [2, 1]
