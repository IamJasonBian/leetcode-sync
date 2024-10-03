class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define the keyboard rows
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        def can_type_in_one_row(word):
            word_set = set(word.lower())
            return word_set.issubset(row1) or word_set.issubset(row2) or word_set.issubset(row3)
        
        # Filter words that can be typed using characters from only one row
        return [word for word in words if can_type_in_one_row(word)]
