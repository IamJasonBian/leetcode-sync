from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_x, max_y, max_z = float('-inf'), float('-inf'), float('-inf')
        
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                max_x = max(max_x, t[0])
                max_y = max(max_y, t[1])
                max_z = max(max_z, t[2])
        
        return max_x == target[0] and max_y == target[1] and max_z == target[2]
