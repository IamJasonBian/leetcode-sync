class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        print(nums)

        '''

        Approach 1:
            Strategy is where and when do you flip the ks:

            * Store all the 1s into a hash map with the largest sequence + indexes
            * 

        Approach 2:
            * Sliding window to keep track of start and end of the ones
            * Grow and strink the window

        '''
        left = 0           # Left pointer of our window
        zeros = 0         # Count of zeros in current window
        max_length = 0    # Maximum length of consecutive ones (including flipped zeros)
        
        for right in range(len(nums)):
            # If we encounter a zero, increment our zero counter
            if nums[right] == 0:
                zeros += 1
            
            # If we have too many zeros, shrink window from left until valid
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # Update max_length with current window size
            max_length = max(max_length, right - left + 1)
        
        return max_length



