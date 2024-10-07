import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Create two lists: one for start times and one for end times
        start_times = [interval[0] for interval in intervals]
        end_times = [interval[1] for interval in intervals]

        # Sort both lists
        start_times.sort()
        end_times.sort()

        # Heapify the end times list
        heapq.heapify(end_times)

        rooms = 0
        max_rooms = 0
        start_ptr = 0
        
        while start_ptr < len(intervals):
            if start_times[start_ptr] < end_times[0]:
                # If a meeting starts before the earliest end time,
                # we need a new room
                rooms += 1
                start_ptr += 1
            else:
                # If a meeting starts after or at the earliest end time,
                # we can reuse that room
                heapq.heappop(end_times)
                rooms -= 1
            
            max_rooms = max(max_rooms, rooms)

        return max_rooms
