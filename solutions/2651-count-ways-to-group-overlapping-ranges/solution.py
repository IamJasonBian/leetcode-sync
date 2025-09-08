class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        result = [ranges[0]]
        for i in range(1, len(ranges)):
            if result[-1][1] >= ranges[i][0]:
                result[-1][1] = max(result[-1][1], ranges[i][1])
            else:
                result.append(ranges[i])
        return int((2 ** len(result)) % ((10 ** 9 ) + 7))           
