class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # init
        output = []
        
        # A function to generate permutations
        def genPerm(curr: List, v: List=[]):
            nonlocal output
            if curr:
                for i,c in enumerate(curr):
                    genPerm(curr[:i] + curr[i+1:], v+[curr[i]])
            else:
                if v:
                   output.append(v)
            return
        
        # send sorted array to generate permutations
        genPerm(sorted(nums))
        
        return output
