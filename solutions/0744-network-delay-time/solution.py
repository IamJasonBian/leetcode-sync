class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        '''
        You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (u_i, v_i, w_i), where u_i is the source node, v_i is the target node, and w_i is the time it takes for a signal to travel from source to target.

        We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

        '''


        '''
            Basically shortest path from all nodes to starting point etc 


        '''

        import heapq
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v,w))
        heap = [(0,k)]
        visited = set()
        max_time = 0
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            max_time = time
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time + weight, neighbor))
        return max_time if len(visited) == n else -1
