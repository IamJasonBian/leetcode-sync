class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x=0
        while x <len(nums):
            if nums[x]<target:
                x+=1
            else:
                return x
        return x
