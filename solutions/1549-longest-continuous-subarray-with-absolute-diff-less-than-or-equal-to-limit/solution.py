class Solution:
        def longestSubarray(self, nums: List[int],
    limit: int) -> int:
          from collections import deque

          l = 0
          max_sub = 0
          min_deque = deque() 
          max_deque = deque()  

          for r in range(len(nums)):

              while min_deque and nums[min_deque[-1]] >= nums[r]:
                  min_deque.pop()
              min_deque.append(r)

              while max_deque and nums[max_deque[-1]] <= nums[r]:
                  max_deque.pop()
              max_deque.append(r)


              while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                  if min_deque[0] == l:
                      min_deque.popleft()
                  if max_deque[0] == l:
                      max_deque.popleft()
                  l += 1

              max_sub = max(max_sub, r - l + 1)

          return max_sub
