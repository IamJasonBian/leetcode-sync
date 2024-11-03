class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        '''

        Set the windows here

        '''


        n = len(nums)
        result = [-1] * n
        prefix = [0] * (n + 1)

        # prefix sum compaction
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(k, n - k):
            window_sum = prefix[i + k + 1] - prefix[i - k]
            result[i] = window_sum // (2 * k + 1)
        return result
        
    
