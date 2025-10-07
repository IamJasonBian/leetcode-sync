class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        print(points)

        '''
        
            There are some spherical balloons tapes onto a flat wall that represents the XY-plane. The ballons are represented as a 2D integer array points where points[i] = [x_start, x_end] denotes a ballon whose horizontal diameter stretches between x_start and x_end.


            Arrows can be shot up directly vertically 

            * No limit to the number of arraos that can be shot
            * Shot arrows keeps traveling up infnitely, bursting any balloons in its path
            Return the minimum number of arrows that must be shot to burst all balloons

        Arrow intervals
            
        '''
        points.sort(key=lambda x: x[1])
        arrows = 0
        end = float('-inf')
        for start, ballon_end in points:
            if start > end:
                arrows += 1
                end = ballon_end
        return arrows





        
