"""Flood Fill

URL: https://leetcode.com/problems/flood-fill/
"""
from collections import deque
from copy import deepcopy
from typing import List, Iterable


class Solution:
    @staticmethod
    def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        result = deepcopy(image)
        color = image[sr][sc]
        if new_color == color:
            return result

        max_height = len(image) - 1
        max_width = len(image[0]) - 1

        points = set()
        queue = deque([(sr, sc)])
        while len(queue):
            y, x = queue.popleft()
            result[y][x] = new_color
            # up
            if y > 0 and result[y - 1][x] == color:
                job = (y - 1, x)
                if job not in points:
                    queue.append(job)
                    points.add(job)
            # down
            if y < max_height and result[y + 1][x] == color:
                job = (y + 1, x)
                if job not in points:
                    queue.append(job)
                    points.add(job)
            # left
            if x > 0 and result[y][x - 1] == color:
                job = (y, x - 1)
                if job not in points:
                    queue.append(job)
                    points.add(job)
            # right
            if x < max_width and result[y][x + 1] == color:
                job = (y, x + 1)
                if job not in points:
                    queue.append(job)
                    points.add(job)

        return result


def test_case_0():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    new_color = 2
    result = Solution.flood_fill(image, sr, sc, new_color)
    assert result == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


def test_case_1():
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    new_color = 2
    result = Solution.flood_fill(image, sr, sc, new_color)
    assert result == [[2, 2, 2], [2, 2, 2]]


def test_case_2():
    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    new_color = 1
    result = Solution.flood_fill(image, sr, sc, new_color)
    assert result == [[0, 0, 0], [0, 1, 1]]
