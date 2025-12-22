import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        g = defaultdict(dict)
        for u, v, w in times:
            g[u][v] = w
        
        d = {k: 0}
        q = [(0, k)]
        while q:

        # weight assignment with variables etc 
        
            dist, u = heapq.heappop(q)
            if dist > d[u]: continue
            for v, w in g[u].items():
                if v not in d or d[u] + w < d[v]:
                    d[v] = d[u] + w
                    heapq.heappush(q, (d[v], v))

        return max(d.values()) if len(d) == n else -1


