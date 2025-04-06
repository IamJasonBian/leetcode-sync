class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def minEatingSpeed(piles: List[int], H: int) -> int:
            def feasible(speed) -> bool:
                # keep in mind that sorting is not needed here because everything descends 
                return sum((pile - 1) // speed + 1 for pile in piles) <= H  # faster

            left, right = 1, max(piles)
            while left < right:

                # we are eatting the piles up to a certain direction
                
                mid = left  + (right - left) // 2
                if feasible(mid):

                    right = mid
                else:
                    left = mid + 1
            return left


        return minEatingSpeed(piles, h)
