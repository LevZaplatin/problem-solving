"""Search Insert Position

URL: https://leetcode.com/problems/search-insert-position/
"""
from typing import List


class Solution:
    @staticmethod
    def search_insert(numbers: List[int], target: int) -> int:
        length = len(numbers)
        minimum = 0
        maximum = length
        split_size = None
        position = length // 2

        while split_size is None or split_size > 0:
            split_size = (maximum - minimum) // 2
            position = minimum + split_size
            number = numbers[position]

            if target > number:
                minimum += split_size
            elif target < number:
                maximum -= split_size
            else:
                break

        return position + 1 if target > numbers[position] else position


def test_case_1():
    nums = [1, 3, 5, 6]
    target = 5
    assert Solution.search_insert(nums, target) == 2


def test_case_2():
    nums = [1, 3, 5, 6]
    target = 2
    assert Solution.search_insert(nums, target) == 1


def test_case_3():
    nums = [1, 3, 5, 6]
    target = 7
    assert Solution.search_insert(nums, target) == 4


def test_case_4():
    nums = [1, 3, 5, 6]
    target = 0
    assert Solution.search_insert(nums, target) == 0


def test_case_5():
    nums = [1]
    target = 0
    assert Solution.search_insert(nums, target) == 0
