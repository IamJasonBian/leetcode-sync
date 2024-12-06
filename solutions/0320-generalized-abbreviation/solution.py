class Solution:
    def store_abbreviations(
        self, abbreviations, word, curr_word, index, abbreviated_count
    ):
        if index == len(word):
            if abbreviated_count > 0:
                curr_word += str(abbreviated_count)
            abbreviations.append(curr_word)
            return
        self.store_abbreviations(
            abbreviations,
            word,
            curr_word
            + (str(abbreviated_count) if abbreviated_count > 0 else "")
            + word[index],
            index + 1,
            0,
        )

        self.store_abbreviations(
            abbreviations, word, curr_word, index + 1, abbreviated_count + 1
        )

    def generateAbbreviations(self, word):
        abbreviations = []
        self.store_abbreviations(abbreviations, word, "", 0, 0)
        return abbreviations
