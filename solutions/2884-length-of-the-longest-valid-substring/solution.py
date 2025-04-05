class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:


        # Optimization Methods:

            # Early Termination with Binary Search
            # Using Trie for Faster Pattern Matching
            # Sliding Window with Optimization

        '''

            max_length = 0
            for i in range(len(word)):
                for j in range(i + 1, len(word) + 1):
                    substring = word[i:j]

                    valid = True
                    for forbidden_str in forbidden:
                        if forbidden_str in substring:
                            valid = False
                            break
            
                    if valid:
                        max_length = max(max_length, len(substring))
            
            return max_length
        
        '''

        forbidden_set = set(forbidden)
        max_forbidden_len = max(len(s) for s in forbidden)

        n = len(word)
        result = 0
        right = n - 1

        print(n)
        print(result)
        print(right)

        for left in range(n - 1, -1, -1):
            for j in range(left, 

            # search space limits because any forbidden substring that is encountered at position j will let us limit our search space 

            
            min(left + max_forbidden_len,
            right + 1)):
                if word[left:j+1] in forbidden_set:
                    right = j - 1
                    break

            result = max(result, right - left + 1)
        return result
