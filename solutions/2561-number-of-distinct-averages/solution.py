class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avgs = set()
        nums_sorted = sorted(nums)
        for i in range(len(nums)//2):
            avgs.add((nums_sorted[i] + nums_sorted[-1-i])/2)
        return len(avgs)    
