class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def condition(mid: int) -> bool:
            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                return nums[mid] >= target
            return target >= nums[0]
        
        if not nums:
            return -1
            
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
                
        if left == len(nums) or nums[left] != target:
            return -1
        return left
