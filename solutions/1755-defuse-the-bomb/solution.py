class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        if k == 0:
            return result
            
        # Calculate initial window sum
        window_sum = 0
        if k > 0:
            for i in range(k):
                window_sum += code[(i + 1) % n]
        else:
            for i in range(abs(k)):
                window_sum += code[(n - 1 - i) % n]
        
        # Update each position
        for i in range(n):
            result[i] = window_sum
            if k > 0:
                window_sum -= code[(i + 1) % n]
                window_sum += code[(i + k + 1) % n]
            else:
                window_sum -= code[(n + i - abs(k)) % n]
                window_sum += code[i % n]
                
        return result
