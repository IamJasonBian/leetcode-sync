class Solution:
    def maxProduct(self, nums):
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            temp = max_prod
            max_prod = max(max_prod * nums[i], min_prod * nums[i], nums[i])
            min_prod = min(temp * nums[i], min_prod * nums[i], nums[i])
            ans = max(ans, max_prod)
            
        return ans
