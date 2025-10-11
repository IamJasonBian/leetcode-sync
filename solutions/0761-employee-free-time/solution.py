class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        # https://leetcode.com/problems/meeting-rooms-ii/description/
        start = []
        end = []
        result = []
        count = 0

        for intervals in schedule:
            for interval in intervals:
                start.append(interval.start)
                end.append(interval.end)

        start.sort()
        end.sort()

        s = e = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                count -= 1
                if count == 0 and end[e] != start[s]:
                    result.append(Interval(end[e], start[s]))
                e += 1
        return result
 

