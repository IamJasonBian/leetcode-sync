from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize a list to store the number of combinations for each amount up to the target amount
        dp = [0] * (amount + 1)
        dp[0] = 1 # There is one way to make change for 0 amount: don't use any coins

        #Double Loop/permuate through every coin
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]

