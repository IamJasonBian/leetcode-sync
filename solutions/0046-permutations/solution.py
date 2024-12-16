class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
            
        for i in range(len(nums)):
            n = nums.pop(0)  # Remove first element
            perms = self.permute(nums)  # Recursive call
            
            # Add back n to each position
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)  # Add n back to restore nums
            
        return result
