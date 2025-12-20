class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        order = []
        while q:
            curr = q.popleft()
            count += 1
            order.append(curr)
            for next in adj[curr]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)

        if count < numCourses:
            return []

        return order
