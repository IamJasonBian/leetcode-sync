class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        '''

            The **CRUX** of https://leetcode.com/problems/max-consecutive-ones/description/ is in the fact that below previously came from a position of data structures having greedy optimal substructure. This means that the 

            **original** “In an array of 0s and 1s, we are to fing length of the longest chain of 1s” 

            statement traverses the whole array one to find the various chains of 1. 
            
            sequences = []  
            cnt = 0
            
        '''

        sequences = []
        cnt = 0
        
        # 70.61, 17.40

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            elif cnt > 0:  # 
                sequences.append(cnt)
                cnt = 0
        
        if cnt > 0:
            sequences.append(cnt)
            
        return max(sequences) if sequences else 0
            
            

        '''

        cnt = 0      # 70.61, 36.58
        cnt_max = 0

        for i in range(len(nums)):
            if nums[i] == 1: 
                cnt += 1    
            else:
                cnt_max = max(cnt, cnt_max)  
                cnt = 0

        return max(cnt, cnt_max)  
        '''
       
