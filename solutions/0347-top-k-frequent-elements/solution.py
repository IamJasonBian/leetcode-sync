from collections import Counter

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)         
        return [key for key, _ in Counter(nums).most_common(k)]


            
