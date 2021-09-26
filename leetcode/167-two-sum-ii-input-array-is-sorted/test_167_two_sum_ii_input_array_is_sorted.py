"""Two Sum II - Input array is sorted

URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


class Solution:
    @staticmethod
    def two_sum(numbers: List[int], target: int) -> List[int]:
        sums = {}
        for index, number in enumerate(numbers, start=1):
            x = target - number
            if index_x := sums.get(x):
                return [index_x, index]
            sums[number] = index


def test_case_1():
    numbers = [2, 7, 11, 15]
    target = 9
    assert Solution.two_sum(numbers, target) == [1, 2]


def test_case_2():
    numbers = [2, 3, 4]
    target = 6
    assert Solution.two_sum(numbers, target) == [1, 3]


def test_case_3():
    numbers = [-1, 0]
    target = -1
    assert Solution.two_sum(numbers, target) == [1, 2]
