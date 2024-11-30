class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        alex=0
        
        while(piles):

            alex+=abs(piles[0]+piles[-2] - piles[-1]+piles[1])
            piles=piles[2:-2]
            
        if alex>0:
            return True
        return False
