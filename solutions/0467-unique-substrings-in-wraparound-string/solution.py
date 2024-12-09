class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        cnt = 0
        seen = {} # longest string ending at char 
        for i in range(len(p)): 
            if 0 < i and (ord(p[i]) - ord(p[i-1])) % 26 != 1: cnt = 0 # reset counter 
            cnt += 1
            seen[p[i]] = max(seen.get(p[i], 0), cnt)
        return sum(seen.values())
