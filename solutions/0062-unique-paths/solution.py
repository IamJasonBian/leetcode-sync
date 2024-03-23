class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the dp array with zeros
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Base case: there is only one way to reach the starting cell
        dp[0][0] = 1
        
        # Fill the first row and first column with 1s
        for i in range(1, m):
            dp[i][0] = 1
        for j in range(1, n):
            dp[0][j] = 1
        
        # Fill the rest of the dp array
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The number of unique paths to reach the bottom-right corner is in the bottom-right cell
        return dp[m-1][n-1]
