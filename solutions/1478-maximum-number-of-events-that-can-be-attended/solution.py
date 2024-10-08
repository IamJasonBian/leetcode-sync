class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        min_heap = []  # min heap of events end time
        events.sort(key = lambda e: e[0])  # sort events by start time

        i = count_events_attended = cur_day = 0
        while i < len(events) or min_heap:
            if not min_heap:
                cur_day = events[i][0]
            
            # add open events for cur_day
            while i < len(events) and events[i][0] <= cur_day:
                heappush(min_heap, events[i][1])
                i += 1

            heappop(min_heap)  # attend the event ends earliest
            count_events_attended += 1

            cur_day += 1
            # remove close events for cur_day
            while min_heap and min_heap[0] < cur_day:
                heappop(min_heap)

        return count_events_attended
