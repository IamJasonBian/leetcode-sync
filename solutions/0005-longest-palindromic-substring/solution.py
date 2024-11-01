class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(start, length):
            substring = s[start:start+length]
            return substring == substring[::-1]
            
        def dfs_with_depth(start, length):
            # Base case
            if length <= 0:
                return False
                
            # Check if current substring is palindrome
            if is_palindrome(start, length):
                return True
                
            # Try smaller lengths from this start point
            return False

        n = len(s)
        max_length = 0
        result = s[0] if s else ""
        
        # Try increasing lengths (iterative deepening)
        for length in range(n, 0, -1):
            found = False
            # Try each starting position
            for start in range(n - length + 1):
                if dfs_with_depth(start, length):
                    result = s[start:start+length]
                    found = True
                    break
            if found:
                break
                
        return result
