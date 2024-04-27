class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        # Sort both arrays in descending order
        jobs.sort(reverse=True)
        workers.sort(reverse=True)
        
        # Initialize the maximum days to 0
        max_days = 0
        
        # Iterate over the sorted jobs and workers
        for i in range(len(jobs)):
            # Calculate the days taken by the current worker to complete the current job
            days = (jobs[i] + workers[i] - 1) // workers[i]
            # Update the maximum days if the current calculation is greater
            max_days = max(max_days, days)
        
        # Return the maximum days, which is the minimum number of days needed
        return max_days
