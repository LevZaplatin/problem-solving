"""Contains Duplicate

URL: https://leetcode.com/problems/contains-duplicate/
"""
from typing import List, Set


class Solution:
    @staticmethod
    def contains_duplicate(nums: List[int]) -> bool:
        uniq_numbers: Set[int] = set()
        for number in nums:
            if number in uniq_numbers:
                return True
            uniq_numbers.add(number)
        return False


def test_case_0():
    numbers = [1, 2, 3, 1]
    result = Solution.contains_duplicate(numbers)
    assert result is True


def test_case_1():
    numbers = [1, 2, 3, 4]
    result = Solution.contains_duplicate(numbers)
    assert result is False


def test_case_2():
    numbers = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result = Solution.contains_duplicate(numbers)
    assert result is True
