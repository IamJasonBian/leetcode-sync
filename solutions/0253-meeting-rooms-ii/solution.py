from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        


        # Separate and sort start and end times
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        
        rooms = 0
        end_pointer = 0
        
        for start in starts:
            # If the current start time is after the earliest ending time
            if start >= ends[end_pointer]:
                # Free up a room
                end_pointer += 1
            else:
                # Need a new room
                rooms += 1
        
        return rooms

