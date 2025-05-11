from typing import List
from collections import defaultdict, deque

class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list and degrees
        adj = defaultdict(list)
        deg = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u] += 1
            deg[v] += 1

        # Find connected components
        visited = [False] * n
        comps = []  # list of (nodes, edge_count)
        for i in range(n):
            if not visited[i]:
                # BFS/DFS to collect component
                queue = deque([i])
                visited[i] = True
                comp_nodes = []
                edges_cnt = 0
                while queue:
                    x = queue.popleft()
                    comp_nodes.append(x)
                    edges_cnt += deg[x]
                    for nei in adj[x]:
                        if not visited[nei]:
                            visited[nei] = True
                            queue.append(nei)
                comps.append((comp_nodes, edges_cnt // 2))

        # Sort components by "efficiency" (edges per node) and then by edge_count.
        # A cycle with m nodes has m edges and thus higher contribution per label than a path
        # of the same size (m-1 edges). Assigning higher labels to more "efficient" components
        # maximizes the total sum.
        comps.sort(key=lambda x: (x[1] / len(x[0]), x[1]), reverse=True)

        # Prepare labels sorted descending
        labels = list(range(1, n+1))
        labels.sort(reverse=True)
        idx = 0

        # Result assignment
        value = [0] * n
        for comp_nodes, e_cnt in comps:
            m = len(comp_nodes)
            block = labels[idx: idx + m]
            idx += m
            # Sort block ascending
            block.sort()

            # Helper: arrange block to maximize adjacent products in a line
            def arrange_line(arr):
                if len(arr) <= 2:
                    return arr
                res = [0] * len(arr)
                l, r, p = 0, len(arr) - 1, 0
                while l <= r:
                    res[l] = arr[p]
                    p += 1
                    l += 1
                    if l <= r:
                        res[r] = arr[p]
                        p += 1
                        r -= 1
                return res

            # Determine component type and order of nodes
            if e_cnt == m:  # cycle
                # Order nodes in cycle by traversal
                start = comp_nodes[0]
                order = [start]
                prev = -1
                curr = start
                while True:
                    found = False
                    for nei in adj[curr]:
                        if nei != prev:
                            order.append(nei)
                            prev, curr = curr, nei
                            found = True
                            break
                    if not found or curr == start:
                        break
                if order and order[-1] == start:
                    order.pop()

                block = arrange_line(block)
            else:  # path or singleton
                # find endpoint (deg==1) if exists, else singleton
                endpoint = comp_nodes[0]
                for x in comp_nodes:
                    if deg[x] == 1:
                        endpoint = x
                        break
                # traverse path from endpoint
                order = []
                prev = -1
                curr = endpoint
                while True:
                    order.append(curr)
                    nxt = None
                    for nei in adj[curr]:
                        if nei != prev:
                            nxt = nei
                            break
                    if nxt is None:
                        break
                    prev, curr = curr, nxt

                block = arrange_line(block)
            # assign values along order (common for both cycle and path)
            for i, node in enumerate(order):
                value[node] = block[i]

        # Compute total score
        res = 0
        for u, v in edges:
            res += value[u] * value[v]
        return res
