class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_max = nums[0]
        local_min = nums[0]
        global_max = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            if num >= 0:
                local_max,local_min = max(num, num*local_max),min(num, num*local_min)
            else:
                local_max,local_min = max(num,num* local_min), min(num,num*local_max)
            global_max = max(global_max,local_max)
        return global_max


        
