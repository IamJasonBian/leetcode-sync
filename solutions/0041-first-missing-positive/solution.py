from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Step 1: Partition the array to move all non-positive numbers to the end
        n = len(nums)
        write_index = 0
        for num in nums:
            if num <= 0:
                continue
            nums[write_index] = num
            write_index += 1
        
        # Step 2: Mark indices based on the absolute value of numbers
        for i in range(write_index):
            num = abs(nums[i])
            if num > n:
                continue
            if nums[num - 1] > 0:
                nums[num - 1] *= -1
        
        # Step 3: Find the first index with a positive value
        for i in range(write_index):
            if nums[i] > 0:
                return i + 1
        
        # Step 4: If all numbers up to n are marked, return n + 1
        return write_index + 1

# Example usage
solution = Solution()
nums = [1, 2, 0]
print(solution.firstMissingPositive(nums))  # Output: 3

