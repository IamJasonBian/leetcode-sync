class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        '''
            Method: We need to make sure that each word (Bucket is fully filled from the text by the output buckets)
            Approach: 
                
        '''
        words = set(words)
        ans = []

        # two pointer traversal 

        for i in range(len(text)):
            for j in range(i , len(text)):
                if text[i:j + 1] in words:
                    ans.append([i,j])

            # check if the stack in words match the text then pop

        return ans




