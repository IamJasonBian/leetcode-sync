class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:


        #1.objective function:
        #count how many times a word is in sequence

        #2.identify base cases:
        #the sequence is length 0 
        #the word either equals the sequence or it doesnt

        #3.write the transition function:
        #dp[i]=dp[i-word_length]+1 if word equals sequence[i-len(word):i]

        #4.order of computation:
        #buttom up

        #5.location of the answer
        #its the highest number in dp
        
        sequence_length=len(sequence)
        word_length=len(word)
        dp=[0]*(sequence_length+1)
        for i in range(word_length,sequence_length+1):
            if word==sequence[i-word_length:i]:
                dp[i]=dp[i-word_length]+1


        return max(dp)
        
        
