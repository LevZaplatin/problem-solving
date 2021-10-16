"""Max Area of Island

URL: https://leetcode.com/problems/max-area-of-island/
"""
from collections import deque
from typing import List


class Solution:
    @staticmethod
    def max_area_of_island(grid: List[List[int]]) -> int:
        max_island_size = 0
        max_height = len(grid) - 1
        max_width = len(grid[0]) - 1
        island_marker = 1

        points = set()
        queue = deque()
        for i in range(max_height + 1):
            for j in range(max_width + 1):
                point = (i, j)
                if point in points:
                    continue
                if grid[i][j] != island_marker:
                    points.add(point)
                    continue

                island_size = 0
                queue.append(point)
                while len(queue):
                    y, x = queue.popleft()
                    if (y, x) in points:
                        continue

                    points.add((y, x))
                    if grid[y][x] == island_marker:
                        island_size += 1
                    # up
                    if y > 0 and grid[y - 1][x] == island_marker:
                        new_point = (y - 1, x)
                        if new_point not in points:
                            queue.append(new_point)
                    # down
                    if y < max_height and grid[y + 1][x] == island_marker:
                        new_point = (y + 1, x)
                        if new_point not in points:
                            queue.append(new_point)
                    # left
                    if x > 0 and grid[y][x - 1] == island_marker:
                        new_point = (y, x - 1)
                        if new_point not in points:
                            queue.append(new_point)
                    # right
                    if x < max_width and grid[y][x + 1] == island_marker:
                        new_point = (y, x + 1)
                        if new_point not in points:
                            queue.append(new_point)
                max_island_size = max(max_island_size, island_size)

        return max_island_size


def test_case_0():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    result = Solution.max_area_of_island(grid)
    assert result == 6


def test_case_1():
    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    result = Solution.max_area_of_island(grid)
    assert result == 0


def test_case_2():
    grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    result = Solution.max_area_of_island(grid)
    assert result == 4
