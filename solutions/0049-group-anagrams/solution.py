from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create set of sets   
        # split into characters
        
       
        ans = defaultdict(list)
        
        for s in strs:
            key = [0] * 26
            for c in s:
                
                key[ord(c) - ord('a')] += 1
                
            key = tuple(key)
            
            ans[key].append(s)
            
        return ans.values()
        
        
