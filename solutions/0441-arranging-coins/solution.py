class Solution:
    def arrangeCoins(self, n: int) -> int:
        previous = 0
        if n ==1:
            return n
        for j in range(1, n+1):
            n-=j
            if  n < 0 :
                previous = j -1
                return previous
