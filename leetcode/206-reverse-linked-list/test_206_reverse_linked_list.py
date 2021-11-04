"""Reverse Linked List

Difficulty: Easy 
URL: https://leetcode.com/problems/reverse-linked-list/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other is None:
            return False

        node = self
        other_node = other
        while node.next:
            if other_node and node.val == other_node.val:
                if node.next or other_node.next:
                    node = node.next
                    other_node = other_node.next
            else:
                return False

        return other_node and node.val == other_node.val


class Solution:
    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        node = head
        while node:
            stack.append(node)
            node = node.next

        new_head = None
        cursor = None
        while stack:
            current_node = stack.pop()
            current_node.next = None
            if new_head is None:
                new_head = current_node
            else:
                cursor.next = current_node
            cursor = current_node

        return new_head


def test_case_0():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = Solution.reverse_list(head)
    expected = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
    assert result == expected


def test_case_1():
    head = ListNode(1, ListNode(2))
    result = Solution.reverse_list(head)
    expected = ListNode(2, ListNode(1))
    assert result == expected


def test_case_2():
    head = None
    result = Solution.reverse_list(head)
    expected = None
    assert result is expected
