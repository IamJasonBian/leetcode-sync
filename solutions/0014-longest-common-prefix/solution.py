class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            if len(strs) == 0: return ""
            elif len(strs) == 1: return strs[0]
            min_s = min(strs)
            max_s = max(strs)
            for idx, ch in enumerate(min_s):
                if max_s[idx] != ch: return min_s[:idx]
            return min_s
