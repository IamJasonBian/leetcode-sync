class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        '''
            * The **range** of a subarray of nums is the diff between largest and smallest element in subarray
            * Range is how long each is, etc
            * 


        '''
        n = len(nums)
        result = 0
        
        # Iterate through all possible starting indices
        for i in range(n):
            min_val = max_val = nums[i]
            # Expand the subarray to the right
            # ah, two pointer since expanding x array either to the left or right doesn't yield anything
            for j in range(i + 1, n):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                result += max_val - min_val
        
        return result
