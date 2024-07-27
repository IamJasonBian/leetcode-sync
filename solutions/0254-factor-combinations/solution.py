class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1:
            return []
        
        factors = []
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        
        factors.sort()
        result = []
        
        def backtrack(index, curr_product, curr_combination):
            if curr_product == n:
                result.append(curr_combination[:])
                return
            
            for i in range(index, len(factors)):
                if curr_product * factors[i] > n:
                    break
                
                curr_combination.append(factors[i])
                backtrack(i, curr_product * factors[i], curr_combination)
                curr_combination.pop()
        
        backtrack(0, 1, [])
        return result

