from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        
        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        distinct = []
        for i in arr:
            if freq[i] == 1:
                distinct.append(i)
        return distinct[k-1] if k <= len(distinct) else ""
