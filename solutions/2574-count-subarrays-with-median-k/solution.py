class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        k_index = nums.index(k)
        tmp = [0] * len(nums)
        for i in range(k_index-1, -1, -1):
            gt = 1 if nums[i] > k else -1
            tmp[i] = tmp[i+1] + gt
        for i in range(k_index+1, len(nums)):
            gt = 1 if nums[i] > k else -1
            tmp[i] = tmp[i-1] + gt

        left_count = Counter(tmp[:k_index+1])
        right_count = Counter(tmp[k_index:])
        ret = 0
        for key in left_count:
            if 1-key in right_count:
                ret += left_count[key] * right_count[1-key]
            if -key in right_count:
                ret += left_count[key] * right_count[-key]
        return ret
