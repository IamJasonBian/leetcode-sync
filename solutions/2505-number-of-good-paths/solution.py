class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        values_to_nodes = {}
        for i, value in enumerate(vals):
            values_to_nodes.setdefault(value, []).append(i)


        dsu = UnionFind(n)
        good_paths = 0

        for value, nodes in sorted(values_to_nodes.items()):
            for node in nodes:
                for neig in adj[node]:
                    if vals[node] >= vals[neig]:
                        dsu.union_set(node, neig)


            group = {}
            for node in nodes:
                group[dsu.find(node)] = group.get(dsu.find(node), 0) + 1

            for size in group.values():
                good_paths += (size * (size + 1)) //2


        return good_paths














