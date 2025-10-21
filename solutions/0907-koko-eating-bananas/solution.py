class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

            left, right = 1, max(piles)
            while left < right:
                def feasible(speed) -> bool: 
                    return sum((pile - 1) // speed + 1 for pile in piles) <= h  
                
                mid = (left + right) // 2
            
                if feasible(mid):
                    right = mid
                else:
                    left = mid + 1
            return left


