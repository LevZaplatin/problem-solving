"""Binary Search

URL: https://leetcode.com/problems/binary-search/
"""
from typing import List


class Solution:
    @staticmethod
    def search(numbers: List[int], target: int) -> int:
        result = -1

        length = len(numbers)
        minimum = 0
        maximum = length
        split_size = None

        while split_size is None or split_size > 0:
            split_size = (maximum - minimum) // 2
            position = minimum + split_size
            number = numbers[position]

            if target > number:
                minimum += split_size
            elif target < number:
                maximum -= split_size
            else:
                result = position
                break

        return result


def test_case_1():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert Solution.search(nums, target) == 4


def test_case_2():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    assert Solution.search(nums, target) == -1


def test_case_3():
    nums = [5]
    target = 5
    assert Solution.search(nums, target) == 0


def test_case_4():
    nums = [2, 5]
    target = 5
    assert Solution.search(nums, target) == 1
