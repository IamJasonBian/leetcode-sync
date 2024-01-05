class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 1
        max_sum = 0
        while j < len(prices):
            if prices[i] >= prices[j] :
                i = j
                                
            else:
                val = prices[j] - prices[i]
                max_sum = max(max_sum,val)
            j += 1
        return max_sum
