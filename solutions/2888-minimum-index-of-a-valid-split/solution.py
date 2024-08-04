class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        d=Counter(nums)
        ct=defaultdict(int)
        m=nums[0]
        n=len(nums)
        for i,x in  enumerate(nums):
            ct[x]+=1
            if ct[x]>ct[m]:
                m=x
            # print(m)
            if ct[m]*2>(i+1) and (d[m]-ct[m])*2>n-i-1:
                return i
        
        return -1;
            

            

