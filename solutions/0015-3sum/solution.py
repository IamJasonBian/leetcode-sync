class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        
        for idx in range(len(nums) - 2):
            a = nums[idx]

            if idx != 0 and a == nums[idx - 1]:
                continue
            l = idx + 1
            r = len(nums) - 1
            
            while l < r:
                b = nums[l]
                c = nums[r]
                threeSum = a + b + c
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    ans.append([a, b, c])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ans
