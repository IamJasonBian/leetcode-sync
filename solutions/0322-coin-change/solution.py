from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0


        '''
                  |1|4|6,7,8,20|
                /     \        \
         |7|20|[]|  |1|6|7,8,20|  |30|20|[]|
                    /        \
            |7|20|[]|    |1|7|8,20|
                         /        \
                 |7|20|[]|    |1|8|20|
                               /      \
                       |7|20|[]|  |1|20|[]|
        '''


        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])


        
        return dp[amount] if dp[amount] != amount + 1 else -1


