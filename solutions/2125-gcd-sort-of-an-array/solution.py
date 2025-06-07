from typing import List
import math
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        # Sieve of Eratosthenes to find smallest prime factors
        max_num = max(nums) + 1
        spf = list(range(max_num))
        for i in range(2, int(math.isqrt(max_num)) + 1):
            if spf[i] == i:  # i is a prime number
                for j in range(i*i, max_num, i):
                    if spf[j] == j:  # not yet marked
                        spf[j] = i
        
        uf = UnionFind(max_num)
        
        # Union numbers with their prime factors
        for num in nums:
            if num == 1:
                return False  # 1 can't be swapped with anything
            x = num
            while x > 1:
                p = spf[x]
                uf.union(p, num)
                x //= p
        
        # Check if each number can be placed in its sorted position
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == sorted_nums[i]:
                continue
            if uf.find(nums[i]) != uf.find(sorted_nums[i]):
                return False
        
        return True

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdSort([7, 21, 3]))  # Output: True
    print(sol.gcdSort([5, 2, 6, 2]))  # Output: False
    print(sol.gcdSort([10, 5, 9, 3, 15]))  # Output: True

