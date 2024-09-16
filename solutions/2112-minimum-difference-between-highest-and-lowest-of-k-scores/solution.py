class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        final=[]
        nums.sort()
        for i in range(len(nums)-(k-1)):
            help=nums[i:i+k]
            score=max(help)-min(help)
            final.append(score)
            #print(help)
        #print(final)
        return min(final)
