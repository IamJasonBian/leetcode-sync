from collections import Counter

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        char_count = Counter(s)
        
        # Check if it's possible to form a palindrome
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        if odd_count > 1:
            return []
        
        # Separate characters into halves and center
        half = []
        center = ''
        for char, count in char_count.items():
            half.extend([char] * (count // 2))
            if count % 2 != 0:
                center = char
        
        # Generate permutations using backtracking
        result = []
        self.backtrack(half, center, [], set(), result)
        return result
    
    def backtrack(self, half, center, current, used, result):
        if len(current) == len(half):
            # Form the palindrome
            palindrome = ''.join(current) + center + ''.join(current[::-1])
            result.append(palindrome)
            return
        
        for i in range(len(half)):
            if i in used or (i > 0 and half[i] == half[i-1] and i-1 not in used):
                continue
            
            used.add(i)
            current.append(half[i])
            self.backtrack(half, center, current, used, result)
            current.pop()
            used.remove(i)
