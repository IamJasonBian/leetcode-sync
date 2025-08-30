from collections import OrderedDict

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        if n == 0:
            return 0
        counter = {}
        for d in str(abs(n)):
            counter[d] = counter.get(d, 0) + 1
        sorted_counter = OrderedDict(
            sorted(counter.items(), key=lambda x: (x[1], int(x[0])))
        )
        return int(next(iter(sorted_counter)))
