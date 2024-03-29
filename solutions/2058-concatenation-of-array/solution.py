from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Using list comprehension for demonstration, but it's essentially the same as the + operator
        ans = [num for num in nums] + [num for num in nums]
        return ans
