class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        if not nums:
            return False
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
                
            # If we cannot determine which side is sorted due to duplicates
            if nums[left] == nums[mid]:
                left += 1
                continue
                
            # Left side is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right side is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
