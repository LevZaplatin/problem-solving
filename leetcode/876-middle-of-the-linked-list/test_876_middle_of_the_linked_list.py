"""Middle of the Linked List

URL: https://leetcode.com/problems/middle-of-the-linked-list/
"""
from typing import Optional
from math import ceil


class ListNode:
    def __init__(self, _value=0, _next=None):
        self.val = _value
        self.next = _next


class Solution:
    @staticmethod
    def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
        middle_node = head
        middle_id = 1
        size_of_list = 1

        node = head
        while True:
            size_of_list += 1
            if ceil(size_of_list / 2) != middle_id:
                middle_node = middle_node.next
                middle_id += 1
            if node.next is None:
                break
            node = node.next

        return middle_node


def test_case_1():
    middle = ListNode(4, ListNode(5, ListNode(6)))
    head = ListNode(1, ListNode(2, ListNode(3, middle)))

    assert Solution.middle_node(head) == middle


def test_case_2():
    middle = ListNode(4, ListNode(5, ListNode(6, ListNode(7))))
    head = ListNode(1, ListNode(2, ListNode(3, middle)))

    assert Solution.middle_node(head) == middle


def test_case_3():
    head = ListNode(1)

    assert Solution.middle_node(head) == head
