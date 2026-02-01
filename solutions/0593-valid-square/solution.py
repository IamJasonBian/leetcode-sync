
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        '''
        Figure out the constructs of a square, 
            * Transformation - Calculate distance from p1 to p2
            * Angle - Calculate angle from ray1 to ray2 
        Just do three (p1 to p2 to p3 to p4)

        '''

        d12 = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
        d13 = (p3[0] - p2[0])**2 + (p3[1] - p2[1])**2
        d14 = (p4[0] - p3[0])**2 + (p4[1] - p3[1])**2
        d23 = (p1[0] - p4[0])**2 + (p1[1] - p4[1])**2
        d24 = (p3[0] - p1[0])**2 + (p3[1] - p1[1])**2
        d34 = (p4[0] - p2[0])**2 + (p4[1] - p2[1])**2

        distances = sorted([d12, d13, d14, d23, d24, d34])

        if distances[0] == 0:
            return False

        if not (distances[0] == distances[1] == distances[2] == distances[3]):
            return False

        if distances[4] != distances[5]:
            return False

        if distances[4] != 2 * distances[0]:
            return False

        return True
