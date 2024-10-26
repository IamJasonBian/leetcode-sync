class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def condition(mid: int) -> bool:
            # If nums[mid] and target are on same side of rotation, direct comparison
            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                return nums[mid] >= target
            # Otherwise, decide based on which side target is on
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
