"""Valid Parentheses

URL: https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    @staticmethod
    def is_valid(string: str) -> bool:
        prevs = []
        open_brackets = {"[", "{", "("}
        close_brackets = {"]", "}", ")"}
        map_brackets = {
            "[": "]",
            "(": ")",
            "{": "}",
        }

        for char in string:
            if len(prevs):
                if char in open_brackets:
                    prevs.append(char)
                if char in close_brackets:
                    prev = prevs.pop()
                    close_bracket = map_brackets.get(prev, None)
                    if close_bracket is None or char != close_bracket:
                        return False
            else:
                prevs.append(char)

        return len(prevs) == 0


def test_case_1():
    string = "()"
    assert Solution.is_valid(string) is True


def test_case_2():
    string = "()[]{}"
    assert Solution.is_valid(string) is True


def test_case_3():
    string = "()"
    assert Solution.is_valid(string) is True


def test_case_4():
    string = "(]"
    assert Solution.is_valid(string) is False


def test_case_5():
    string = "([)]"
    assert Solution.is_valid(string) is False


def test_case_6():
    string = "){"
    assert Solution.is_valid(string) is False


def test_case_7():
    string = "({[)"
    assert Solution.is_valid(string) is False


def test_case_8():
    string = "{[]}"
    assert Solution.is_valid(string) is True


def test_case_9():
    string = "))"
    assert Solution.is_valid(string) is False
