class Solution:
    def check_in_bounds(self, m, n, max_row_size, max_col_size):
        if m < 0 or m >= max_row_size:
            return False
        if n < 0 or n >= max_col_size:
            return False
        return True

    def solve(self, i1, j1, i2, j2, grid, dp):
        # Out of bounds check and thorn check
        if (
            not self.check_in_bounds(i1, j1, len(grid), len(grid[0]))
            or not self.check_in_bounds(i2, j2, len(grid), len(grid[0]))
            or grid[i1][j1] == -1
            or grid[i2][j2] == -1
        ):
            return float("-inf")

        # Cache value

        if (i1, j1, i2, j2) in dp:
            return dp[(i1, j1, i2, j2)]

        # Base Case

        # If both person1 and person 2 have reach bottom corner
        if (
            i1 == len(grid) - 1
            and j1 == len(grid[0]) - 1
            and i2 == len(grid) - 1
            and j2 == len(grid[0]) - 1
        ):
            return grid[i1][j1]

        # If person1 has reached the bottom corner
        elif (i1 == len(grid) - 1 and j1 == len(grid[0]) - 1) and (
            i2 != len(grid) - 1 and j2 != len(grid[0]) - 1
        ):
            return grid[i1][j1]

        # If person2 has reached the bottom corner
        elif (i2 == len(grid) - 1 and j2 == len(grid[0]) - 1) and (
            i1 != len(grid) - 1 and j1 != len(grid[0]) - 1
        ):
            return grid[i2][j2]

        # Get current cherry count
        c = 0

        if i1 == i2 and j1 == j2:
            c += grid[i1][j1]
        else:
            c += grid[i1][j1] + grid[i2][j2]

        # Hypo
        f1 = self.solve(i1 + 1, j1, i2 + 1, j2, grid, dp)
        f2 = self.solve(i1, j1 + 1, i2, j2 + 1, grid, dp)
        f3 = self.solve(i1 + 1, j1, i2, j2 + 1, grid, dp)
        f4 = self.solve(i1, j1 + 1, i2 + 1, j2, grid, dp)

        dp[(i1, j1, i2, j2)] = max(f1, f2, f3, f4) + c

        # Induction
        return dp[(i1, j1, i2, j2)]

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {}

        val = self.solve(0, 0, 0, 0, grid, dp)
        if val == float("-inf"):
            return 0
        return val
