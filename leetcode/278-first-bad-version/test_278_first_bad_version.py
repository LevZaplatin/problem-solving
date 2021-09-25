"""First Bad Version

URL: https://leetcode.com/problems/first-bad-version/
"""


class Solution:
    def __init__(self, bad_version: int):
        self.bad_version = bad_version

    def is_bad_version(self, version) -> bool:
        return version >= self.bad_version

    def first_bad_version(self, current_version: int) -> int:
        i = 1
        minimum = None
        maximum = current_version
        while True:
            prev_version = (maximum - (2 ** i))
            if self.is_bad_version(prev_version):
                i += 1
            else:
                minimum = prev_version
                break

        split_size = None
        while split_size is None or split_size > 0:
            diff = maximum - minimum
            if diff > 1:
                split_size = diff // 2
            else:
                split_size = diff

            current = minimum + split_size
            if self.is_bad_version(current):
                maximum -= split_size
            else:
                minimum += split_size

        return minimum + 1


def test_case_1():
    current_version = 5
    bad_version = 4
    solution = Solution(bad_version)
    assert solution.first_bad_version(current_version) == 4


def test_case_2():
    current_version = 1
    bad_version = 1
    solution = Solution(bad_version)
    assert solution.first_bad_version(current_version) == 1
