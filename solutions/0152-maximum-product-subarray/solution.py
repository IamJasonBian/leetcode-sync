class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        if len(nums) == 1:
            return nums[0]

        max_so_far = nums[0]
        min_so_far = nums[0]
        prefix = max_so_far

        for i in range(1, len(nums)): 

            cand = nums[i]
            print("res: " + str(nums[i]) + " idx: " + str(i))
            print(f"res: {nums[i]}, idx: {i}, prefix[i]: {cand}, prefix[i-1]: {prefix}")
           

            # Simulation of x state up one

            temp_max = max(cand, max(max_so_far * cand, min_so_far * cand))
            min_so_far = min(cand, min(max_so_far * cand, min_so_far*cand))

            max_so_far = temp_max
            prefix = max(max_so_far, prefix)
            
        return prefix

        
        
       
