import time
from typing import List
from sortedcontainers import SortedList
from math import inf

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        total_start_time = time.perf_counter()
        n = len(nums)
        
        if n < x * k:
            return -1
        
        # Time the efficient median and cost computation
        cost_calc_start = time.perf_counter()
        
        # Initialize costs array
        costs = [None] * (n - x + 1)
        
        # Initialize two balanced sorted lists for efficient median tracking
        upper = SortedList()
        lower = SortedList()
        su = sl = 0  # Running sums for upper and lower lists
        
        for i, v in enumerate(nums):
            # Add new element to appropriate list
            if not upper or upper[0] <= v:
                upper.add(v)
                su += v
            else:
                lower.add(v)
                sl += v
            
            # Remove element that's no longer in the window
            if i >= x:
                vv = nums[i-x]
                if vv >= upper[0]:
                    upper.remove(vv)
                    su -= vv
                else:
                    lower.remove(vv)
                    sl -= vv
            
            # Rebalance the lists to maintain median property
            while len(upper) > len(lower) + 1:
                v = upper[0]
                upper.remove(v)
                su -= v
                lower.add(v)
                sl += v
            while len(upper) < len(lower):
                v = lower[-1]
                lower.remove(v)
                sl -= v
                upper.add(v)
                su += v
            
            # Calculate cost for complete window
            if i >= x - 1:
                costs[i - x + 1] = su - sl - upper[0] * (len(upper) - len(lower))
        
        cost_calc_end = time.perf_counter()
        print(f"Efficient cost calculation took {cost_calc_end - cost_calc_start:.6f} seconds")
        
        # Create intervals array with start, end, and cost
        intervals_start = time.perf_counter()
        intervals = [(i, i + x - 1, costs[i]) for i in range(len(costs))]
        
        # Sort intervals by end position for DP
        intervals.sort(key=lambda x: x[1])
        intervals_end = time.perf_counter()
        print(f"Creating and sorting intervals took {intervals_end - intervals_start:.6f} seconds")
        
        # Precompute previous non-overlapping intervals
        prev_calc_start = time.perf_counter()
        prev_intervals = [0] * len(intervals)
        
        for i in range(1, len(intervals)):
            start, _, _ = intervals[i]
            
            # Binary search to find previous non-overlapping interval
            left, right = 0, i - 1
            prev = 0
            while left <= right:
                mid = (left + right) // 2
                if intervals[mid][1] < start:
                    prev = mid + 1
                    left = mid + 1
                else:
                    right = mid - 1
            
            prev_intervals[i] = prev
        
        prev_calc_end = time.perf_counter()
        print(f"Precomputing previous intervals took {prev_calc_end - prev_calc_start:.6f} seconds")
        
        # Dynamic programming for optimal interval selection
        dp_start = time.perf_counter()
        dp = [[inf] * (k + 1) for _ in range(len(intervals) + 1)]
        dp[0][0] = 0
        
        for i in range(1, len(intervals) + 1):
            dp[i][0] = 0  # Base case: no segments needed means zero cost
            
            for j in range(1, k + 1):
                # Option 1: Skip this interval
                dp[i][j] = dp[i - 1][j]
                
                # Option 2: Use this interval
                start, end, cost = intervals[i - 1]
                prev = prev_intervals[i - 1]
                
                # Only consider this option if we have enough previous intervals
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[prev][j - 1] + cost)
        
        dp_end = time.perf_counter()
        print(f"DP computation took {dp_end - dp_start:.6f} seconds")
        
        result = dp[len(intervals)][k]
        
        total_end_time = time.perf_counter()
        print(f"Total execution time: {total_end_time - total_start_time:.6f} seconds")
        return result if result != float('inf') else -1
