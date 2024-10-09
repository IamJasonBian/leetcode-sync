class Solution:
    
        
    '''

    Starter:
    
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1261804973/

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    '''
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:  # Not enough days for a transaction.
            return 0

        dp = [[0] * 2 for _ in range(n)]  # dp[i][0]: Not holding stock. dp[i][1]: Holding stock.
        dp[0][1] = -prices[0]  # Cost of buying stock on day 0.

        for i in range(1, n):
            # Max profit not holding stock, not holding yesterday or sell today.
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            
            # Max profit holding stock, holding yesterday or buy today, account for cooldown. dp[i-1][0] = dp[i-2][0] if no cooldown yesterday, no need for seperate.
            dp[i][1] = max(dp[i-1][1], (dp[i-2][0] - prices[i]) if i > 1 else -prices[i]) # If i == 1, can only buy today.
            
        return dp[n-1][0]  # Max profit last day not holding

