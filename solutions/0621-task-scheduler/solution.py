from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_count = list(task_counts.values()).count(max_freq)

        min_intervals = (max_freq - 1) * (n + 1) + max_count
        return max(min_intervals, len(tasks))
