"""Reverse Words in a String III

URL: https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


class Solution:
    @staticmethod
    def reverse_words(sentence: str) -> str:
        last_char = len(sentence) - 1
        last_start_word = 0
        new_sentence = ""
        for index, char in enumerate(sentence):
            is_space = sentence[index] == " "
            is_last_char = index == last_char
            if is_space or is_last_char:
                word_index = 0
                word_length = index - last_start_word
                if is_last_char:
                    word_length += 1

                while word_index < word_length:
                    word_reverse_index = last_start_word + word_length - word_index - 1
                    new_sentence += sentence[word_reverse_index]
                    word_index += 1

                last_start_word = index
                if is_space:
                    last_start_word += 1
                    new_sentence += " "

        return new_sentence


def test_case_1():
    s = "Let's take LeetCode contest"
    assert Solution.reverse_words(s) == "s'teL ekat edoCteeL tsetnoc"


def test_case_2():
    s = "God Ding"
    assert Solution.reverse_words(s) == "doG gniD"
