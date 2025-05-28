from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visits = defaultdict(list)
        for user, time, site in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            user_visits[user].append(site)
        
        pattern_counts = defaultdict(int)
        for sites in user_visits.values():
            for pattern in set(combinations(sites, 3)):
                pattern_counts[pattern] += 1
        
        if not pattern_counts:
            return []
        
        max_count = max(pattern_counts.values())
        candidates = [pattern for pattern, count in pattern_counts.items() if count == max_count]
        
        return list(min(candidates))
