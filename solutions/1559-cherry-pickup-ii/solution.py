from typing import List
from itertools import product

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(COLS)]
        cache = {}

        for r in reversed(range(ROWS)):
            cur_dp = [[0] * COLS for _ in range(COLS)]
            for c1 in range(COLS):
                for c2 in range(c1, COLS):
                    max_cherries = grid[r][c1] + (grid[r][c2] if c1 != c2 else  0)
                    for c1_d, c2_d in product([-1,  0,  1], repeat=2):
                        nc1, nc2 = c1 + c1_d, c2 + c2_d
                        if  0 <= nc1 < COLS and  0 <= nc2 < COLS:
                            max_cherries = max(max_cherries, grid[r][c1] + (grid[r][c2] if c1 != c2 else  0) + dp[nc1][nc2])
                    cur_dp[c1][c2] = max_cherries
            dp = cur_dp

        return dp[0][COLS -  1]

