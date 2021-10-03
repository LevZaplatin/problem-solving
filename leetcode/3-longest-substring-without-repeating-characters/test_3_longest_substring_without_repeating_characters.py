"""Longest Substring Without Repeating Characters

URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from collections import deque


class Solution:
    """
    Runtime: 52 ms, faster than 93.15% of Python3 online submissions for Longest Substring Without Repeating Characters.
    Memory Usage: 14.5 MB, less than 24.55% of Python3 online submissions for Longest Substring Without Repeating Characters.
    """

    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        length = len(s)

        sub_dict = dict()
        start = 0
        index = 0
        maximum = 0
        while index < length:
            char = s[index]
            char_index = sub_dict.get(char)
            if char_index is not None and char_index > start:
                start += char_index - start
            index += 1
            sub_dict[char] = index
            maximum = max(maximum, index - start)

        return maximum

    @staticmethod
    def length_of_longest_substring_v2(s: str) -> int:
        pass


def test_case_1():
    s = "abcabcbb"
    assert Solution.length_of_longest_substring(s) == 3


def test_case_2():
    s = "bbbbb"
    assert Solution.length_of_longest_substring(s) == 1


def test_case_3():
    s = "pwwkew"
    assert Solution.length_of_longest_substring(s) == 3


def test_case_4():
    s = ""
    assert Solution.length_of_longest_substring(s) == 0


def test_case_5():
    s = "au"
    assert Solution.length_of_longest_substring(s) == 2


def test_case_6():
    s = "aab"
    assert Solution.length_of_longest_substring(s) == 2


def test_case_7():
    s = "aabaab!bb"
    assert Solution.length_of_longest_substring(s) == 3
