class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        count = {'a': 0, 'b': 0, 'c': 0}
        n = len(s)
        
        # Count total occurrences of each character
        for char in s:
            count[char] += 1
        
        # Check if it's possible to take k of each character
        if any(count[char] < k for char in 'abc'):
            return -1
        
        left = 0
        result = n
        
        for right in range(n):
            count[s[right]] -= 1
            
            while any(count[char] < k for char in 'abc'):
                count[s[left]] += 1
                left += 1
            
            result = min(result, n - (right - left + 1))
        
        return result
