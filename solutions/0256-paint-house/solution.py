from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        n = len(costs)
        dp = [[0, 0, 0] for _ in range(n)]
        
        # Initialize the DP table for the first house
        dp[0] = costs[0]
        
        # Calculate the minimum cost for each house
        for i in range(1, n):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        
        # The minimum cost to paint all houses is the minimum of the costs to paint the last house with each color
        return min(dp[-1])
