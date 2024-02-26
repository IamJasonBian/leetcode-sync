class Solution:
    def findGCD(self, nums: List[int]) -> int:

        min_num = min(nums)
        max_num = max(nums)

        divisor = min_num
        dividend = max_num

        reminder = dividend % divisor

        while reminder:
            dividend = divisor
            divisor = reminder
            reminder = dividend % divisor

        return divisor
        
