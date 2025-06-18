from typing import List, Set

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        result = []
        
        for word in words:
            if not word:
                continue
            word_set.remove(word)
            dp = [False] * (len(word) + 1)
            dp[0] = True
            
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break
            
            if dp[-1]:
                result.append(word)
            word_set.add(word)
            
        return result

