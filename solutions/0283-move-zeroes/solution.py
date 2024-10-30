class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0

        # Move all non-zero elements to the beginning of the array
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[lastNonZeroFoundAt] = nums[current]
                lastNonZeroFoundAt += 1

        # Fill the remaining positions with zeros
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
