"""
This solution uses a Sorted List with Binary Search approach to efficiently maintain 
and search through a dynamic list of sentences. The sentences are kept sorted in 
lexicographical order, and binary search (via bisect) is used to quickly find the 
range of sentences matching the current prefix. Matching sentences are then sorted 
by their frequency (hotness) and lexicographical order for ties, returning the top 3.
"""

from bisect import bisect_left, bisect_right

class AutocompleteSystem:

    def __init__(self, sentences, times):
        
        # Dictionary to store sentence counts (frequency)
        self.sentenceCount = {}
        
        # Sorted list of sentences
        self.sortedSentences = []
        
        # Current prefix being typed
        self.prefix = ""
        
        # Initialize data structures
        for sentence, time in zip(sentences, times):
            self.sentenceCount[sentence] = time
            self.sortedSentences.append(sentence)
        
        # Sort sentences lexicographically
        self.sortedSentences.sort()
    
    def input(self, character):
        
        # If the character is '#', save the current sentence and reset prefix
        if character == '#':
            self.sentenceCount[self.prefix] = self.sentenceCount.get(self.prefix, 0) + 1
            
            # If it's a new sentence, insert it into sorted list using binary search
            if self.prefix not in self.sortedSentences:
                insertPos = bisect_left(self.sortedSentences, self.prefix)
                self.sortedSentences.insert(insertPos, self.prefix)
            
            self.prefix = ""
            return []
        
        # Append typed character to prefix
        self.prefix += character
        
        # Find start index of matches using binary search
        startIndex = bisect_left(self.sortedSentences, self.prefix)
        
        # Find end index by searching with prefix + '{' (character after 'z' in ASCII)
        endIndex = bisect_right(self.sortedSentences, self.prefix + '{')
        
        # Extract matched sentences
        matchedSentences = self.sortedSentences[startIndex:endIndex]
        
        # Sort matches by frequency descending, then lexicographically
        matchedSentences.sort(key=lambda sentence: (-self.sentenceCount[sentence], sentence))
        
        # Return top 3 matches
        return matchedSentences[:3]
