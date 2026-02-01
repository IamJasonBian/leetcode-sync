class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n < 2:
            return 0

        # Left - Max Profit from one transaction in prices[0:i+1]

        left = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left[i] = max(left[i - 1], prices[i] - min_price)

        # Left Slides and then Right --> 
        # Right - Max Profit from one transaction in prices[i:n]
        right = [0] * n
        max_price = prices[n - 1]
        for i in range(n - 2, 0, -1):
            max_price = max(max_price, prices[i])
            right[i] = max(right[i + 1], max_price - prices[i])
        
        # Combine: best split point for two transactions
        # Temporal seperation
        return max(left[i] + right[i] for i in range(n))
