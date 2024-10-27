class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def condition(value) -> bool:
            if nums[value + 1] < nums[value]:
                return True


        left, right = 0,len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
        
