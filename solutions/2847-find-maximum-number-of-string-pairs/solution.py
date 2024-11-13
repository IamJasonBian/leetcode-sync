class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        seen = set()
        
        for i in range(len(words)):

            curr_word = words[i]
            reversed_word = curr_word[::-1]
            if reversed_word in seen:
                count += 1
            # reverses in this case goes backwards as well
            seen.add(curr_word)
            
        return count
