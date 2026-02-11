class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for i in counter:
            if i == 1:
                continue
            cur = 1
            num = i
            while counter[num] > 1 and counter[num**2]:
                num = num**2
                cur += 2
            ans = max(ans,cur)
        ans2 = counter[1]
        if ans2 % 2 == 0:
            ans2 -= 1
        print(ans,ans2)
        return max(ans,ans2)
