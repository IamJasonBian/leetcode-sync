class Solution:
    def subsetsWithDup(self, nums):
        n = len(nums)
        ans = []
        current_set = []
        nums.sort()

        def subset(idx):
            if idx >= n:
                ans.append(current_set[:])
                return
            
            current_set.append(nums[idx])
            subset(idx + 1)
            current_set.pop()
            
            while idx + 1 < n and nums[idx] == nums[idx + 1]:
                idx += 1
            
            subset(idx + 1)
        
        subset(0)
        return ans
