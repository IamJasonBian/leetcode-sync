import bisect

class MyCalendarTwo:
    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        left = bisect.bisect_right(self.ends, start)
        right = bisect.bisect_left(self.starts, end)
        overlap_starts = self.starts[left:right]
        overlap_ends = self.ends[left:right]
        bisect.insort(overlap_starts, start)
        bisect.insort(overlap_ends, end)

        i = j = 0
        active = 0
        while i < len(overlap_starts) and j < len(overlap_ends):
            if overlap_starts[i] < overlap_ends[j]:
                active += 1
                if active >= 3:
                    return False
                i += 1
            else:
                active -= 1
                j += 1
        
        bisect.insort(self.starts, start)
        bisect.insort(self.ends, end)
        return True
