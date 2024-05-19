class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # max profit matrix
        #mm = []
        profit = 0
        
        for i in range(1, len(prices)):
            '''
            for j in range(i + 1, len(prices)):
                
                max_profit = 0
                
                profit = prices[j] - prices[i]
            '''
            if prices[i] > prices[i - 1]:
                #max_profit = profit
                profit += prices[i] - prices[i - 1]
                #mm.append(max_profit)
                #print(mm)
                
        return profit           
        #return max(mm)
    
        
    '''  
        
    * Each day, you may decide to buy and/ or sell the stock.
    * You can hold at most one share of the stock
    * You can buy it then sell it same day
    * Since this solution relies multiple peaks: 
    
        * Let see what happens when we go forward just a single peak
        * With this implementation you could theoretically get slightly more profit
    
    
    Find max profit:
        
        * Have to buy on day 2 and sell on day 3
        * Need to calculate every permutation of profit from this
            * Essentially how far into the future can we hold the stock
        * But at this point you would need a release mechanism
        * Look ahead one? 
        * Why does greedy work
        
    '''
