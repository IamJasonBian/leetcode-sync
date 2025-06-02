from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        """
        Calculate minimum initial health needed for knight to rescue princess.
        
        Approach: Dynamic Programming (Bottom-up from destination)
        - Work backwards from princess to knight's starting position
        - At each cell, calculate minimum health needed to complete the journey
        - Ensure health never drops to 0 or below
        
        Time: O(m*n), Space: O(m*n)
        """
        
        if not dungeon or not dungeon[0]:
            return 1
        
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        

        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])

        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                min_health_needed = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_health_needed - dungeon[i][j])
        
        return dp[0][0]
