class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        
        n = len(cost)
        answer = [0] * n
        answer[0] = cost[0]
        min_cost = answer[0]
        
        for i in range(1, n):
            answer[i] = min(min_cost, cost[i])
            min_cost = min(min_cost, answer[i])
        
        return answer
