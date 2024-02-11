class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n +  1)  # Create a list of size n+1 with all elements initialized to  0
        
        # Base cases: the cost to reach the first step is just the cost of the first step
        dp[0] = cost[0]
        dp[1] = cost[1]

        print(dp[0])
        
        for i in range(2, n):
            # Calculate the minimum cost to reach the current step
            dp[i] = min(dp[i -  1], dp[i -  2]) + cost[i]
        
        # Return the minimum cost to reach the last step
        return min(dp[n-2], dp[n-1])
