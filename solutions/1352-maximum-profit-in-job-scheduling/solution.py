import heapq
from typing import List

class Job:
    def __init__(self, start: int, end: int, profit: int):
        self.start = start
        self.end = end
        self.profit = profit

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([Job(s, e, p) for s, e, p in zip(startTime, endTime, profit)], 
                     key=lambda x: x.end)
        
        
        dp = [(0, 0)]  
        
        for job in jobs:
           
            left, right = 0, len(dp)
            while left < right:
                mid = (left + right) // 2
                if dp[mid][0] <= job.start:
                    left = mid + 1
                else:
                    right = mid
            
            max_profit_before = dp[right - 1][1] if right > 0 else 0
            current_profit = max_profit_before + job.profit
            
            if not dp or current_profit > dp[-1][1]:
                dp.append((job.end, current_profit))
        
        return dp[-1][1] if dp else 0
