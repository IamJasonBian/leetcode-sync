from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        running_sum = 0
        count = 0


        '''


            for i in range(n):
                current_sum = 0
                for j in range(i, n):
                    current_sum += nums[j]
                    if current_sum == k:
                        count += 1

                                            \section*{Mathematical Formulation}

                    \subsection*{Prefix Sum Definition}
                    For each index $i$ in $0 \leq i < n$:
                    \[
                    prefix[i] = \begin{cases} 
                        nums[0] & \text{if } i = 0 \\
                        prefix[i-1] + nums[i] & \text{if } i > 0
                    \end{cases}
                    \]

                    \subsection*{Subarray Sum Property}
                    For any subarray $nums[i..j]$ where $0 \leq i \leq j < n$, its sum can be expressed as:
                    \[
                    sum(nums[i..j]) = prefix[j] - prefix[i-1] \quad \text{(with } prefix[-1] = 0 \text{)}
                    \]

                    \subsection*{Key Insight}
                    We need to find all pairs $(i,j)$ such that:
                    \[
                    prefix[j] - prefix[i-1] = k
                    \]
                    which can be rewritten as:
                    \[
                    prefix[j] - k = prefix[i-1]
                    \]

[1,1,1]
2
[1,2,3]
3
[1, -1, 2, -2, 3, -3]
-1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, -1, -3, -5, -7, -9, -11, -13, -15, -17, -19, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]
17

        '''

        
        for num in nums:
            running_sum += num
            difference = running_sum - k
            if difference in prefix_sum:
                count += prefix_sum[difference]
                # another left that holds the different
                print (difference )
            prefix_sum[running_sum] += 1
        
                    
        return count
