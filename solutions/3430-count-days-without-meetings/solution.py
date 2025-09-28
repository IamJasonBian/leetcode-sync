class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = itemgetter(0))

        i = 0
        s, e = meetings[0]
        while i + 1 < len(meetings):
            start, end = meetings[i]
            next_start, next_end = meetings[i + 1]
            merged: tuple[int, int]

            if end >= next_start:
                merged = start, max(end, next_end)
                meetings[i:i+2] = [merged]
            else:
                days -= end - start + 1
                i += 1
        else:
            last_start, last_end = meetings[-1]
            days -= last_end - last_start + 1
        return days
        
            
