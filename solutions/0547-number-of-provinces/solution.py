class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Matrices denote what other matrices are connected with each other

        visited = set()

        def dfs(city):
            for n, c in enumerate(isConnected[city]):
                if c == 1 and n not in visited:
                    visited.add(n)
                    dfs(n)

        provinces = 0
        for c in range(len(isConnected)):
            if c not in visited:
                provinces += 1
                dfs(c)

        return provinces

