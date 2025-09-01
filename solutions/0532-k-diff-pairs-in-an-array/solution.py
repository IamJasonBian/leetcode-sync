from collections import Counter

class Solution:
    def findPairs(self, nums, k):



        result = 0
        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                # threshold stacking 

                result += 1
                
            elif k == 0 and counter[x] > 1:

                # nums = [1,3,1,5,4], k = 0 case
                # in-place diffs etc

                result += 1
        return result
