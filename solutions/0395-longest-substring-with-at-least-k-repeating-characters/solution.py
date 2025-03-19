class Solution(object):
    def longestSubstring(self, s, k):

        if len(s) < k:
            return 0
        
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        for char in char_count:
            if char_count[char] < k:

                return max(self.longestSubstring(sub, k) for sub in s.split(char))
        
        return len(s)
