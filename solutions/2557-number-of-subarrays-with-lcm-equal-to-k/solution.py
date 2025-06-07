from typing import List
import math

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        """
        Count subarrays where the LCM of all elements equals k.
        
        Args:
            nums: List of integers
            k: Target LCM value
            
        Returns:
            Number of subarrays with LCM equal to k
            
        Example:
            >>> sol = Solution()
            >>> sol.subarrayLCM([3,6,2,7,1], 6)
            4
            >>> sol.subarrayLCM([3], 2)
            0
        """
        def lcm(a: int, b: int) -> int:
            """Helper function to compute LCM of two numbers."""
            return a * b // math.gcd(a, b) if a and b else 0
        
        count = 0
        n = len(nums)
        
        for i in range(n):
            current_lcm = 1  
            for j in range(i, n):
                current_lcm = lcm(current_lcm, nums[j])

                if current_lcm > k:
                    break

                if current_lcm == k:
                    count += 1
        
        return count

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.subarrayLCM([3,6,2,7,1], 6))  # Output: 4
    print(sol.subarrayLCM([3], 2))          # Output: 0
