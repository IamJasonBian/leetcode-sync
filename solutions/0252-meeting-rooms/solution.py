class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort the intervals based on start time
        intervals.sort(key=lambda x: x[0])

        # [1] Note that a post sorted interval will work because the next immediate interval should always be more than the last interval's end
        # [2] What about the edge case where
            # * [0, 5]
            # * [4, 10] (10 check against 5)
            # * [5, 6] (6 check against 10)

        # Check for overlaps
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True

