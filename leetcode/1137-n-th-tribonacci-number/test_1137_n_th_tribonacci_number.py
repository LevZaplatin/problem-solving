"""N-th Tribonacci Number

URL: https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    @staticmethod
    def tribonacci(n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1

        first = 0
        second = 1
        third = 1
        for i in range(n):
            new_value = first + second + third
            first = second
            second = third
            third = new_value

        return first


def test_case_0():
    n = 4
    result = Solution.tribonacci(n)
    assert result == 4


def test_case_1():
    n = 0
    result = Solution.tribonacci(n)
    assert result == 0


def test_case_2():
    n = 1
    result = Solution.tribonacci(n)
    assert result == 1


def test_case_3():
    n = 2
    result = Solution.tribonacci(n)
    assert result == 1


def test_case_4():
    n = 25
    result = Solution.tribonacci(n)
    assert result == 1389537


def test_case_5():
    n = 5
    result = Solution.tribonacci(n)
    assert result == 7


def test_case_7():
    n = 7
    result = Solution.tribonacci(n)
    assert result == 24


def test_case_8():
    n = 3
    result = Solution.tribonacci(n)
    assert result == 2
