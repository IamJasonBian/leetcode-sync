class Solution:
    def countDays(self, total_days: int, meetings: list[list[int]]) -> int:
        if not meetings:
            return total_days

        meetings.sort()  # Sort by start day
        current_start, current_end = meetings[0]
        covered_days = 0

        for meeting_start, meeting_end in meetings[1:]:
            if meeting_start <= current_end + 1:  # Handle adjacent days
                current_end = max(current_end, meeting_end)
            else:
                covered_days += current_end - current_start + 1
                current_start, current_end = meeting_start, meeting_end

        # Add the last meeting block
        covered_days += current_end - current_start + 1

        return max(total_days - covered_days, 0)
