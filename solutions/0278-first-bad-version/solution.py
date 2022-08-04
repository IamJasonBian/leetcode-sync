class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        h = n
        while l <= h:
            
            # All subsequent bad versions will go bad, so binary search can be used to catch the top end
            
            mid = (l+h)//2
            if isBadVersion(mid) and isBadVersion(mid-1)==False:
                return mid
            if isBadVersion(mid) == False:
                l = mid+1
            elif isBadVersion(mid) and isBadVersion(mid-1):
                h = mid-1
        return -1
