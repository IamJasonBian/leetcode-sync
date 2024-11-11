from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        '''
        Find the diagonal order of elements in a 2D array, including jagged arrays.

        Args:
            nums (List[List[int]]): A 2D array of integers, possibly jagged.

        Returns:
            List[int]: All elements of nums in diagonal order.
        '''
        diagonals = defaultdict(list)
        max_key = 0
        
        # Step 1 & 2: Traverse the 2D array and group elements by diagonal sum
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                diagonals[i + j].append(val)
                max_key = max(max_key, i + j)
        
        # Step 3 & 4: Collect elements in diagonal order
        result = []
        for diagonal_sum in range(max_key + 1):
            result.extend(reversed(diagonals[diagonal_sum]))
        
        return result
