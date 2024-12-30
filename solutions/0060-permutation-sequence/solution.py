class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create dictionary of available numbers
        numbers = {i: str(i) for i in range(1, n + 1)}
        
        # Calculate factorials we'll need
        factorial = 1
        for i in range(1, n):
            factorial *= i
        
        # Convert k to 0-based index
        k = k - 1
        
        result = []
        # For each position
        for i in range(n - 1, 0, -1):
            # Calculate which number goes in current position
            index = k // factorial
            k = k % factorial
            factorial = factorial // i
            
            # Find the number at that index from available numbers
            count = 0
            for num in sorted(numbers.keys()):
                if count == index:
                    result.append(numbers[num])
                    del numbers[num]
                    break
                count += 1
        
        # Append the last remaining number
        result.append(numbers[list(numbers.keys())[0]])
        
        return ''.join(result)
