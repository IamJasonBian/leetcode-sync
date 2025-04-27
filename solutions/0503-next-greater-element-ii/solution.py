class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        n=len(nums)
        res=[0]*n
        
        for i in range(n-1,-1,-1):
            st.append(nums[i])
        for i in range(n-1,-1,-1):
            while  st and st[-1]<=nums[i]:
                st.pop()
            if len(st)==0:
                res[i]=-1
            else:
                res[i]=st[-1]
            st.append(nums[i])
        return res
            
        
