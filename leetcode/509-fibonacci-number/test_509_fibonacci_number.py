"""Fibonacci Number

URL: https://leetcode.com/problems/fibonacci-number/
"""


class Solution:
    @staticmethod
    def fib(n: int) -> int:
        if n < 2:
            return n

        prev = 0
        current = 1
        for i in range(n):
            new_value = prev + current
            prev = current
            current = new_value

        return prev


def test_case_0():
    n = 2
    result = Solution.fib(n)
    assert result == 1


def test_case_1():
    n = 3
    result = Solution.fib(n)
    assert result == 2


def test_case_2():
    n = 4
    result = Solution.fib(n)
    assert result == 3


def test_case_3():
    n = 1
    result = Solution.fib(n)
    assert result == 1


def test_case_4():
    n = 0
    result = Solution.fib(n)
    assert result == 0
