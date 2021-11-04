"""Merge Two Sorted Lists

Difficulty: Easy 
URL: https://leetcode.com/problems/merge-two-sorted-lists/
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
            if node.val == other_node.val:
                if node.next or other_node.next:
                    node = node.next
                    other_node = other_node.next
            else:
                return False

        return other_node and node.val == other_node.val


class Solution:
    @staticmethod
    def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cursor_l1 = l1
        cursor_l2 = l2
        list_node = None
        cursor = None
        while cursor_l1 or cursor_l2:
            if cursor_l1 and cursor_l2:
                if cursor_l1.val > cursor_l2.val:
                    next_node = ListNode(cursor_l2.val)
                    cursor_l2 = cursor_l2.next
                else:
                    next_node = ListNode(cursor_l1.val)
                    cursor_l1 = cursor_l1.next
            elif cursor_l1:
                next_node = ListNode(cursor_l1.val)
                cursor_l1 = cursor_l1.next
            else:
                next_node = ListNode(cursor_l2.val)
                cursor_l2 = cursor_l2.next

            if list_node is None:
                list_node = next_node
                cursor = next_node
            else:
                cursor.next = next_node
                cursor = next_node

        return list_node


def test_case_0():
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    result = Solution.merge_two_lists(l1, l2)
    expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    assert result == expected


def test_case_1():
    l1 = None
    l2 = None

    result = Solution.merge_two_lists(l1, l2)
    expected = None
    assert result is expected


def test_case_2():
    l1 = None
    l2 = ListNode(0)

    result = Solution.merge_two_lists(l1, l2)
    expected = ListNode(0)
    assert result == expected
