"""Reverse String

URL: https://leetcode.com/problems/reverse-string/
"""
from typing import List


class Solution:
    @staticmethod
    def reverse_string(string_list: List[str]) -> None:
        length = len(string_list)
        index = 0
        half_length = length // 2
        while index < half_length:
            reverse_index = length - index - 1
            string_list[index], string_list[reverse_index] = string_list[reverse_index], string_list[index]
            index += 1


def test_case_1():
    s = ["h", "e", "l", "l", "o"]
    Solution.reverse_string(s)
    assert s == ["o", "l", "l", "e", "h"]


def test_case_2():
    s = ["H", "a", "n", "n", "a", "h"]
    Solution.reverse_string(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
