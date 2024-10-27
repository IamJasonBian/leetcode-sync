class Solution:
    def equalFrequency(self, word: str) -> bool:
        N = len(word)
        
        uniq_letters = set(word)
        # a. Word of same letter: 'aaaaa'
        # b. All frequency of letter is 1: 'abcde'
        if len(uniq_letters) == 1 or len(uniq_letters) == N:
            return True

        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1
        
        count = Counter(freq)
        del count[0]
            
        if len(count) != 2:
            return False
        
        k1, k2 = min(count.keys()), max(count.keys())
        
        # c-i
        if k1 == count[k1] == 1:
            return True
        
        # c-ii
        if k2 - k1 == 1 and count[k2] == 1:
            return True
        
        return False
       
