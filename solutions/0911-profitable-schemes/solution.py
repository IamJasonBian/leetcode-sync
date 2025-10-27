class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        d =[[0] * (n +1) for i in range(minProfit + 1)]
        d[0]= [1] * (n +1)
        for j in range(0, len(group)):
            for p in range(minProfit, -1, -1):
                for i in range(n, group[j] -1, -1):  
                    d[p][i] += d[max(p- profit[j] , 0 )][i - group[j]]         
        return d[minProfit][n] % (10**9+7)
