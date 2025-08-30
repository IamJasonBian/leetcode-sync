class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        sorted_res =  sorted(freq.keys(), key=lambda x: (-freq[x], x))
        return sorted_res[:k]
