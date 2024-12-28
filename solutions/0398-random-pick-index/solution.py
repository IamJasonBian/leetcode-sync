from random import randint

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.indices = defaultdict(list)

    def pick(self, target: int) -> int:
        if target in self.indices:
            return self.indices[target][
                randint(0, len(self.indices[target])-1)
            ]
        
        r = None
        count = 0

        for i, n in enumerate(self.nums):
            if n == target:
                if r is None or randint(0, count) == 0:
                    r = i
                count += 1

            self.indices[n].append(i)
        return r
