class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # Add Seed nodes to queue to start BFS 
        queue = deque([[element, 1] for element in nestedList])
        total = 0

        while queue:
            cur_element, depth = queue.pop()
            if cur_element.isInteger():
                total += cur_element.getInteger()*depth
            else:
                for nested_element in cur_element.getList():
                    queue.appendleft([nested_element, depth+1])
        
        return total
    
