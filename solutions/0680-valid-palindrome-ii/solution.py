class Solution:

    '''
   def validPalindrome(self, s: str) -> bool:
    def isPalindrome(s):
        return s == s[::-1]
    
    def remove(s, idx):
        return s[:idx] + s[idx+1:]
        
    for i in range(len(s)):
        temp = remove(s, i)
        if isPalindrome(temp):
            return True
            
    return False
    '''

    def validPalindrome(self, s: str) -> bool:
        # Two pointer approach
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try removing either character and check if remaining is palindrome
                skip_left = s[left+1:right+1]
                skip_right = s[left:right]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            left += 1
            right -= 1
            
        return True
