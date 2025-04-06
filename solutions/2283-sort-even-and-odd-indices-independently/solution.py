class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(0, n, 2):
            for j in range(0, n - i - 2, 2):
                if nums[j] > nums[j + 2]:
                    nums[j], nums[j + 2] = nums[j + 2], nums[j]

        for i in range(1, n, 2):
            for j in range(1, n - i - 1, 2):
                if nums[j] < nums[j + 2]:
                    nums[j], nums[j + 2] = nums[j + 2], nums[j]
        return nums
