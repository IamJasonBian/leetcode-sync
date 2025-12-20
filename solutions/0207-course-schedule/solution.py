from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for p in prerequisites:
            adj[p[1]].append(p[0])
            indegree[p[0]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            curr = q.popleft()
            count += 1
            for next in adj[curr]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)

        return count == numCourses
