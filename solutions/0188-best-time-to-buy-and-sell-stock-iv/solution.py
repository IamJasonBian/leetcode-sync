# Extended Kadane's implementation

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if 2*k >= len(prices): 
            return sum(max(0, prices[i]-prices[i-1]) for i in range(1, len(prices)))
        
        
        # Note that the DPs here are the best possible implementation for that specific value key at that point in time
        
        pnl = [0]*len(prices)
        for _ in range(k):
            val = 0
            for i in range(1, len(pnl)): 
                val = max(pnl[i], val + prices[i] - prices[i-1]) 
                pnl[i] = max(pnl[i-1], val)
        return pnl[-1]
