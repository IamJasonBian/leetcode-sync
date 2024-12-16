class Solution:
    def numSquares(self, n: int) -> int:
        """
        Find the least number of perfect square numbers that sum to n.
        Uses dynamic programming approach.
        
        Args:
            n: Target number
            
        Returns:
            Minimum number of perfect squares needed to sum to n
        """
        # Initialize dp array with worst case (all 1s)
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Build solution for all numbers from 1 to n
        for i in range(1, n + 1):
            # Try all perfect squares less than or equal to i
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
                
        return dp[n]
