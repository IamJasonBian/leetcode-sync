class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.abbrev_map = {}
        self.word_set = set(dictionary)
        
        # Preprocess the dictionary
        for word in dictionary:
            abbr = self.get_abbreviation(word)
            if abbr not in self.abbrev_map:
                self.abbrev_map[abbr] = set()
            self.abbrev_map[abbr].add(word)
    
    def isUnique(self, word: str) -> bool:
        abbr = self.get_abbreviation(word)
        
        # If the abbreviation isn't in our map, it's definitely unique
        if abbr not in self.abbrev_map:
            return True
        
        # If the abbreviation exists, it's only unique if the only word with this abbreviation is the input word itself
        words_with_abbr = self.abbrev_map[abbr]
        return len(words_with_abbr) == 1 and word in words_with_abbr
    
    def get_abbreviation(self, word: str) -> str:
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]
