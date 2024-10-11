class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        list1=[]
        for i in range(len(nums)-1):
            list1.append(sum(nums[i:i+2%(len(nums))]))
        return sorted(set(list1))!=sorted(list1)
