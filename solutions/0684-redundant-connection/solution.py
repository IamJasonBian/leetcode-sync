class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def make_set(n):
            """Initialize union-find structures for n elements."""
            return {
                'parent': list(range(n)),
                'rank': [0] * n,
                'count': n
            }

        def find(uf, x):

            if uf['parent'][x] != x:
                uf['parent'][x] = find(uf, uf['parent'][x])
            return uf['parent'][x]
        
        def union(uf, x, y):

            root_x, root_y = find(uf, x), find(uf, y)
            if root_x == root_y:
                return False

            if uf['rank'][root_x] < uf['rank'][root_y]:
                root_x, root_y = root_y, root_x

            uf['parent'][root_y] = root_x
            if uf['rank'][root_x] == uf['rank'][root_y]:
                uf['rank'][root_x] += 1

            uf['count'] -= 1
            return True

        uf = make_set(len(edges)+1)

        result = []
        #union permanently loads into place
        for edge in edges:
            if not union(uf, edge[0], edge[1]):
                result = edge
        return result


        print(f"Sets: {uf['count']}")
