from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if the total number of elements is a multiple of n
        if len(original) != m * n:
            return []
        
        # Construct the 2D array
        array_2d = []
        for i in range(0, len(original), n):
            array_2d.append(original[i:i+n])
        
        return array_2d
