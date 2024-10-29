class Solution:
    def minimalKSum(self, A: List[int], k: int) -> int:
        A = sorted(list(set(A)))
        n = len(A)
        
        if A[n - 1] <= k + n:
            return (k + n) * (k + n + 1) // 2 - sum(A)

        lft, rgt = 0, n - 1
        while rgt > lft:
            mid = (lft + rgt) // 2
            if A[mid] - mid <= k:
                lft = mid + 1
            else:
                rgt = mid

        return (k + lft) * (k + lft + 1) // 2 - sum(A[:lft])
        
