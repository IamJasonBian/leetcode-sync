class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        return [[area//x,x] for x in range(int(area**0.5),0,-1) if area%x==0][0]
        
