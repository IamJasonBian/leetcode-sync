from collections import Counter

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        n = len(s)
        left = 0
        right = 0
        max_length = 0
        char_count = Counter()

        for r in range(n): 
            char_count[s[r]] += 1
            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_length = max(max_length, r  - left + 1)
        
        return max_length
        

