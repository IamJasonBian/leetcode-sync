class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        disc = [0] * n
        low = [0] * n
        time = 1
        res = []
        
        def dfs(curr, prev):
            nonlocal time
            disc[curr] = low[curr] = time
            time += 1
            
            for next_node in graph[curr]:
                if not disc[next_node]:
                    dfs(next_node, curr)
                    low[curr] = min(low[curr], low[next_node])
                elif next_node != prev:
                    low[curr] = min(low[curr], disc[next_node])
                
                if low[next_node] > disc[curr]:
                    res.append([curr, next_node])
        
        dfs(0, -1)
        return res
