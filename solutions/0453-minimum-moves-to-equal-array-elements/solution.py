class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        Given an array nums, returns minimum moves required to make all elements equal.
        One move: increment n-1 elements by 1.
        Key insight: Instead of incrementing n-1 elements, we can decrement 1 element.
        This is equivalent because relative difference remains same.
        """
        if not nums:
            return 0
            
        min_num = min(nums)
        moves = 0
        
        # Each number needs to be decremented until it equals the minimum
        for num in nums:
            moves += num - min_num
            
        return moves
