class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        start=0
        end=0
        ans=0
        freq={}
        while end<n:
            freq[nums[end]]=freq.get(nums[end],0)+1
            while freq[nums[end]]>k:
                freq[nums[start]]-=1
                start+=1
            ans=max(ans,end-start+1)
            end+=1  
        return ans  
