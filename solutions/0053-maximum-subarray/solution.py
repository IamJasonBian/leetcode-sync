class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Brute force

        '''
        m = nums[0]

        for i in range(len(nums)):
            c = 0
            for j in range (i, len(nums)):
                c += nums[j]
                m = max(m, c)
        return m    
        
        #possible number is contributing (making sum larger)
        # 4
        # -1, 2 
        # 2 doesn't know values in front
        # sum is 5
        # 2 comes bundled with -1
        # -2 if we extend
        # -2 added to positive 3
        # -2 can be added to 3
        # never add a negative previous sum
        # Largest ended sum is 3, 
        # 
        # Curr Sum 3 + 4 = 7
        '''
        # 
        m = nums[0]
        c = 0

        for n in nums:
            c = max(c, 0)
            c += n
            m = max(m, c)
        return m
