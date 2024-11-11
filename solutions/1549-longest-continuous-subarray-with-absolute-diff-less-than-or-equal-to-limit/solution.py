from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        longest = 0

        for right, num in enumerate(nums):
            # Maintain max_deque
            while max_deque and nums[max_deque[-1]] <= num:
                max_deque.pop()
            max_deque.append(right)

            # Maintain min_deque
            while min_deque and nums[min_deque[-1]] >= num:
                min_deque.pop()
            min_deque.append(right)

            # Shrink window if necessary
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Update longest subarray
            longest = max(longest, right - left + 1)

        return longest
