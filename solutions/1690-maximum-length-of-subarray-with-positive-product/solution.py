class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0

        # pos neg split
        pos = 0  # length of subarray with positive product
        neg = 0   # length of subarray with negative product
        
        for num in nums:
            if num > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            elif num < 0:
                new_pos = neg + 1 if neg > 0 else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            else:
                pos = neg = 0
            
            max_len = max(max_len, pos)
        
        return max_len
