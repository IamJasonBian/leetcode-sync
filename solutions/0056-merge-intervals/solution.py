class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #Sort Solution            
        intervals.sort(key=lambda value: value[0])
        
        init = intervals[0]
        start = init[0]
        end = init[1]
        result = []
                
        for i in range(1, len(intervals)):
            start_loc = intervals[i][0]
            end_loc = intervals[i][1]
            
            if start_loc > end:
                result.append([start,end])
                start = start_loc
                
            if end_loc > end:
                end = end_loc
        
        #Append Last Result
        result.append([start,end])
                
        return(result)
            
        
