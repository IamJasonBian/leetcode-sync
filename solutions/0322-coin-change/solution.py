from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp list with infinity for all amounts except  0
        dp = [float('inf')] * (amount +  1)
        dp[0] =  0  # Base case:  0 coins needed to make up amount  0
        
        # Iterate through each coin denomination
        for coin in coins:
            # Update dp values for all amounts greater than or equal to coin value
            for x in range(coin, amount +  1):
                # Take the minimum between the current dp value and the dp value for the amount minus the coin value plus one
                dp[x] = min(dp[x], dp[x - coin] +  1)
        
        # Return -1 if no combination can sum to the amount, otherwise return the minimum number of coins
        return -1 if dp[amount] == float('inf') else dp[amount]

