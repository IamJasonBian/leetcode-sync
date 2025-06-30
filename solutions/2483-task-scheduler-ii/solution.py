class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        count = 0
        lastPos = defaultdict(int)
        for task in tasks:
            count += 1
            if task in lastPos and count - lastPos[task] <= space: 
                count += space - (count - lastPos[task]) + 1
            lastPos[task] = count
        return count
        
