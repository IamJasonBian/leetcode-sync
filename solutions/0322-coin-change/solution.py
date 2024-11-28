class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1
                
                
                )

        # [0,1,1,2,2,1,2,2,3,3,2,3] dp[11] = 3        
        return dp[amount] if dp[amount] != float('inf') else -1 
