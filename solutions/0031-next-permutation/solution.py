class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
		
        # Find longest maximal permutation
        i = len(nums) - 1
        while i > 1 and nums[i] <= nums[i - 1]:
            i -= 1

        # Find first element to swap
        pivot = i - 1
        i = len(nums) - 1
        while i > pivot and nums[pivot] >= nums[i]:
            i -= 1

        if pivot == i:
            pivot = -1
        else:
            nums[i], nums[pivot] = nums[pivot], nums[i]

        # Reverse maximal sub permutation
        for i in range(1, (len(nums) - pivot + 1) // 2):
            x, y = pivot + i, -i
            nums[x], nums[y] = nums[y], nums[x]
        
        
        
