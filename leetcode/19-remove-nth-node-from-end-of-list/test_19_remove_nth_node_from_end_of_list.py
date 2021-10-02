"""Remove Nth Node From End of List

URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
from typing import Optional


class ListNode:
    def __init__(self, _value=0, _next=None):
        self.val = _value
        self.next = _next

    def __str__(self):
        nodes = [self.val]
        node = self.next

        if node:
            while node.next:
                nodes.append(node.val)
                node = node.next
            nodes.append(node.val)

        return ", ".join(map(str, nodes))


class Solution:
    @staticmethod
    def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_target_node = head
        size_of_list = 0

        node = head
        while True:
            size_of_list += 1
            possible_target_id = size_of_list - n - 1
            if possible_target_id > 0:
                prev_target_node = prev_target_node.next
            if node.next is None:
                break
            node = node.next

        if n == 1 and size_of_list == 1:
            return None

        if possible_target_id < 0:
            # the first object
            head = head.next
        else:
            target_node = prev_target_node.next
            if target_node.next:
                prev_target_node.next = target_node.next
            else:
                # the last object
                prev_target_node.next = None

        return head


def test_case_1():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

    assert str(Solution.remove_nth_from_end(head, 2)) == "1, 2, 3, 4, 6"


def test_case_2():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    assert str(Solution.remove_nth_from_end(head, 2)) == "1, 2, 3, 5"


def test_case_3():
    head = ListNode(1)

    assert Solution.remove_nth_from_end(head, 1) is None


def test_case_4():
    head = ListNode(1, ListNode(2))

    assert str(Solution.remove_nth_from_end(head, 2)) == "2"


def test_case_5():
    head = ListNode(1, ListNode(2))

    assert str(Solution.remove_nth_from_end(head, 1)) == "1"


def test_case_6():
    head = ListNode(1, ListNode(2, ListNode(3)))

    assert str(Solution.remove_nth_from_end(head, 2)) == "1, 3"


def test_case_7():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

    assert str(Solution.remove_nth_from_end(head, 6)) == "2, 3, 4, 5, 6"
