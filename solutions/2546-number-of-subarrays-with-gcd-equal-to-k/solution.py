from typing import List
import math

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        """
        Count subarrays where the GCD of all elements equals k.
        
        Args:
            nums: List of integers
            k: Target GCD value
            
        Returns:
            Number of subarrays with GCD equal to k
            
        Example:
            >>> sol = Solution()
            >>> sol.subarrayGCD([9,3,1,2,6,3], 3)
            4
            >>> sol.subarrayGCD([4], 7)
            0
        """

        count = 0
        n = len(nums)
        for i in range(n):
            current_gcd = 0
            for j in range(i, n):
                # collapse subarrays
                current_gcd = math.gcd(current_gcd, nums[j])
                if current_gcd < k:
                    break
                    
                if current_gcd == k:
                    count += 1
        
        return count

# this runs in leetcode
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarrayGCD([9,3,1,2,6,3], 3))  
    print(sol.subarrayGCD([4], 7))           
