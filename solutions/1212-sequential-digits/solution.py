class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def gen_sequential_numbers(max_num):
            result = []
            for length in range(2, 10):
                for start in range(1, 10 - length + 1):
                    num = int(''.join(str(start + i) for i in range(length)))
                    if num > max_num:
                        if length == 2:
                            return result  
                        break
                    result.append(num)
            return result
        all_sequential = gen_sequential_numbers(high)
        result = [num for num in all_sequential if num >= low]
        
        return result
