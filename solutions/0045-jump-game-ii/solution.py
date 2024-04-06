class Solution:
    def jump(self, nums: List[int]) -> int:

        # DP-able
        # Greedy Solution O(n) -> DP O(n^2)
        # BFS

        res = 0
        l = r = 0

        while r < len(nums) - 1:
            # move L to range
            # Move R to range
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest 
            res += 1
        return res 


