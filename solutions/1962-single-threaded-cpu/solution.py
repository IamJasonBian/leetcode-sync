import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        tasks.sort(key=lambda x: (x[0], x[2]))
        
        ls, order = [], []
        j = 0
        time = 0

        while j < n or ls:
            if not ls:
                time = max(time, tasks[j][0])
                
            while j < n and tasks[j][0] <= time:
                heapq.heappush(ls, (tasks[j][1], tasks[j][2]))
                j += 1
                
            processing_time, original_idx = heapq.heappop(ls)
            order.append(original_idx)
            time += processing_time
    
        return order
