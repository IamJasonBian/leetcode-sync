class Solution:
    def longestPalindrome(self, s: str) -> int:
        x = Counter(s)
        total = 0
        checkodd = False

        for i in x.values():
            if i % 2 == 0:
                total += i
            elif not checkodd:
                total += i
                checkodd = True
            else:
                total += i-1
        return total

        
