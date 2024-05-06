class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping from digits to letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        # Base case: if digits is empty, return an empty list
        if not digits:
            return []
        
        # Recursive case: generate combinations for the rest of the string
        if len(digits) == 1:
            return list(digit_to_letters[digits[0]])
        
        # Combine letters for the current digit with combinations for the rest of the string
        combinations = []
        for letter in digit_to_letters[digits[0]]:
            for combination in self.letterCombinations(digits[1:]):
                combinations.append(letter + combination)
        
        return combinations

