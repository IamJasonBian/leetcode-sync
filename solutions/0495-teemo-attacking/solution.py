class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        if not timeSeries:

            return 0

        poisoned = duration
        for i in range(1, len(timeSeries)):
            poisoned += duration - max(0, timeSeries[i-1]+duration - timeSeries[i])

        return poisoned
