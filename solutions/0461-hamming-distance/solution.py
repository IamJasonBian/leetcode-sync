class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans=x^y
        x=bin(ans)
        return x.count('1')
        
