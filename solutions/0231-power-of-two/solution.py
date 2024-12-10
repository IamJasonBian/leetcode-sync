class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n==1):return True
        s = bin(n)
        s = s[2:]
        if (s[0]!= '1'):
            return False
        elif (s.count('1')>1):
            return False
        else:
            return True
