# SortedDict in python is similar to ordered_map in C++

from sortedcontainers import SortedDict

class SummaryRanges:

    def __init__(self):
        self.treeMap = SortedDict()

    def addNum(self, value: int) -> None:
        # Insert in the treeMap
        self.treeMap[value] = True

    # Building the Interval every time getInterval is called
    
    def getIntervals(self) -> List[List[int]]:
        res = []
        for n in self.treeMap:
            # If range is continuing then res should have been nonEmpty and the last range's 2nd value
            # should be less than current by 1
            if res and res[-1][1] + 1 == n:
                res[-1][1] = n
            else:
                res.append([n,n])
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
