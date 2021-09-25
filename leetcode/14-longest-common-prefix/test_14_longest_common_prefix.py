"""Longest Common Prefix

URL: https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


class Solution:
    @staticmethod
    def longest_common_prefix(strings: List[str]) -> str:
        length = len(strings)
        prefixes = dict()

        size = 1
        counter = 1
        counter_prefixes = length
        while counter == 1 and counter_prefixes == length:
            new_prefixes = dict()
            counter_prefixes = 0
            for s in strings:
                if size > len(s):
                    continue
                counter_prefixes += 1
                prefix = s[:size]
                new_prefixes[prefix] = new_prefixes.get(prefix, 0) + 1

            counter = len(new_prefixes)

            if len(new_prefixes) == 1 and counter_prefixes == length:
                prefixes = new_prefixes
                size += 1

        keys = list(prefixes.keys())
        if len(keys):
            return keys[0]
        return ""


def test_case_1():
    strings = ["flower", "flow", "flight"]
    assert Solution.longest_common_prefix(strings) == "fl"


def test_case_2():
    strings = ["dog", "racecar", "car"]
    assert Solution.longest_common_prefix(strings) == ""


def test_case_3():
    strings = [""]
    assert Solution.longest_common_prefix(strings) == ""


def test_case_4():
    strings = ["a"]
    assert Solution.longest_common_prefix(strings) == "a"


def test_case_5():
    strings = ["", "b"]
    assert Solution.longest_common_prefix(strings) == ""
