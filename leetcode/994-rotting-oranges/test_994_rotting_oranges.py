"""Rotting Oranges

URL: https://leetcode.com/problems/rotting-oranges/
"""
from collections import deque
from typing import List


class Solution:
    @staticmethod
    def oranges_rotting(grid: List[List[int]]) -> int:
        rottens = deque()
        kill = 0
        fresh = 0
        rotten_count = 0
        empty = set()

        y_length = len(grid)
        max_y_index = y_length - 1
        if y_length == 0:
            return -1
        x_length = len(grid[0])
        max_x_index = x_length - 1

        for y in range(y_length):
            for x in range(x_length):
                value = grid[y][x]
                if value:
                    if value == 2:
                        rotten_count += 1
                        rottens.append((x, y))
                    else:
                        fresh += 1
                else:
                    empty.add((x, y))

        minutes = 0
        while rottens:
            new_rottens = []
            while rottens:
                rotten = rottens.popleft()
                if rotten in empty:
                    continue
                kill += 1
                empty.add(rotten)
                x, y = rotten

                # top
                if y > 0 and grid[y - 1][x] == 1:
                    new_rottens.append((x, y - 1))
                # down
                if y < max_y_index and grid[y + 1][x] == 1:
                    new_rottens.append((x, y + 1))
                # left
                if x > 0 and grid[y][x - 1] == 1:
                    new_rottens.append((x - 1, y))
                # right
                if x < max_x_index and grid[y][x + 1] == 1:
                    new_rottens.append((x + 1, y))

            if new_rottens:
                rottens.extendleft(new_rottens)
                if rottens and (kill - rotten_count) != fresh:
                    minutes += 1

        if (kill - rotten_count) != fresh:
            return -1

        return minutes


def test_case_0():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result = Solution.oranges_rotting(grid)
    assert result == 4


def test_case_1():
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    result = Solution.oranges_rotting(grid)
    assert result == -1


def test_case_2():
    grid = [[0, 2]]
    result = Solution.oranges_rotting(grid)
    assert result == 0
