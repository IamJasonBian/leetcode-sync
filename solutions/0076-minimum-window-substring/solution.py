class Solution:
    def minWindow(self, s: str, t: str) -> str:

        targetLen = len(t)
        if targetLen > len(s) or targetLen == 0:
            return ""
            
        targetCt = defaultdict(int)
        for letter in t:
            targetCt[letter] += 1

        l = 0
        min_len = float('inf')
        min_window = ""
        
        for r in range(len(s)):
            if s[r] in targetCt:
                targetCt[s[r]] -= 1
                if targetCt[s[r]] >= 0:
                    targetLen -= 1
            
            while targetLen == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = s[l:r+1]
                
                if s[l] in targetCt:
                    targetCt[s[l]] += 1
                    if targetCt[s[l]] > 0:
                        targetLen += 1
                l += 1
                    
        return min_window
