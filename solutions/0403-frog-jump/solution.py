class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        memo = {}
        
        def can_reach(pos, k):
            if pos == stones[-1]:
                return True
            if (pos, k) in memo:
                return memo[(pos, k)]
            
            for next_k in [k-1, k, k+1]:
                if next_k > 0 and pos + next_k in stone_set:
                    if can_reach(pos + next_k, next_k):
                        memo[(pos, k)] = True
                        return True
            memo[(pos, k)] = False
            return False
        
        return stones[1] == 1 and can_reach(1, 1) if len(stones) > 1 else True
