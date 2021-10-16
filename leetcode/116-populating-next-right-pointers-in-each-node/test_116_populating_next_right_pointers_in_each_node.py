"""Populating Next Right Pointers in Each Node

URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.next == other.next
        return False


class Solution:
    @staticmethod
    def connect(root: Node) -> Node:
        queue = deque([root])

        while queue:
            nodes = []
            prev = None
            while queue:
                node = queue.popleft()
                if prev:
                    prev.next = node
                if node:
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                prev = node
            queue.extend(nodes)

        return root
