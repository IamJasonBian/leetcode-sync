class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = {}
        
        for i in nums:
            if i in hs:
                hs[i] += 1
            else:
                hs[i] = 1
                
        keys_with_more_than_one_hit = [key for key, value in hs.items() if value > 1]
    
        return keys_with_more_than_one_hit
            
            
