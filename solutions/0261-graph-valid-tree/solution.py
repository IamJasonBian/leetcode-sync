class UnionFind:
    def __init__(self, elements):
        self.parents = {}
        self.rank = {}
        self.number_of_elements = elements

        for i in range(elements):
            # Set all parents to be their on parent
            self.parents[i] = i
            self.rank[i] = 0

    def find(self, element):
        while element != self.parents[element]:
            element = self.parents[element]
        return self.parents[element]

    def union(self, first_element, second_element):
        parent_one = self.find(first_element)
        parent_two = self.find(second_element)

        # Can't union nodes that have the same parent
        if parent_one == parent_two:
            return False
        
        if self.rank[parent_one] > self.rank[parent_two]:
            self.parents[parent_two] = parent_one
        else:
            self.parents[parent_one] = parent_two
            self.rank[parent_two] += 1
        self.number_of_elements -= 1
        return True
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        union_find = UnionFind(n)

        for current_edge in edges:
            union_find.union(current_edge[0], current_edge[1])
        
        return union_find.number_of_elements == 1
    
