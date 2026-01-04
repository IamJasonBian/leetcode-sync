class Solution:
    def largestEven(self, s: str) -> str:
        last_even = s.rfind('2')
        if last_even == -1:
            return ""
        return s[:last_even + 1]
