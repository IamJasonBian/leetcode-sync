class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if int(str(dividend / divisor).split(".")[0]) == 2 ** 31:
            return 2147483647
        return int(str(dividend / divisor).split(".")[0])
        
