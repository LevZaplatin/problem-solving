"""Merge Two Binary Trees

URL: https://leetcode.com/problems/merge-two-binary-trees/
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val
        return False


class Solution:
    @staticmethod
    def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not (root1 or root2):
            return None
        new_tree = TreeNode()
        queue = deque([(new_tree, root1, root2)])
        while queue:
            tree, tree1, tree2 = queue.popleft()
            if (tree1 and tree1.left) or (tree2 and tree2.left):
                tree.left = TreeNode()
            if (tree1 and tree1.right) or (tree2 and tree2.right):
                tree.right = TreeNode()
            if tree1 and tree2:
                tree.val = tree1.val + tree2.val
                queue.append((tree.left, tree1.left, tree2.left))
                queue.append((tree.right, tree1.right, tree2.right))
            elif tree1:
                tree.val = tree1.val
                queue.append((tree.left, tree1.left, None))
                queue.append((tree.right, tree1.right, None))
            elif tree2:
                tree.val = tree2.val
                queue.append((tree.left, None, tree2.left))
                queue.append((tree.right, None, tree2.right))
            else:
                continue

        return new_tree


def test_case_0():
    root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    result = Solution.merge_trees(root1, root2)
    assert result == TreeNode(3, TreeNode(4, TreeNode(5), TreeNode(4)), TreeNode(5, None, TreeNode(7)))


def test_case_1():
    root1 = None
    root2 = None
    result = Solution.merge_trees(root1, root2)
    assert result is None


def test_case_2():
    root1 = None
    root2 = TreeNode(1)
    result = Solution.merge_trees(root1, root2)
    assert result == TreeNode(1)
