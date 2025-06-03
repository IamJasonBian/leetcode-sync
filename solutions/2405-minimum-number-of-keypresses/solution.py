from collections import Counter
class Solution:
    def minimumKeypresses(self, s: str) -> int:

        counts = (Counter(s))
        frequencies = sorted(counts.values(), reverse=True)
        print(frequencies)

        total_keypresses = 0
        
        for i in range(min(9, len(frequencies))):
            total_keypresses += frequencies[i] * 1
        
        for i in range(9, min(18, len(frequencies))):
            total_keypresses += frequencies[i] * 2
        
        for i in range(18, len(frequencies)):
            total_keypresses += frequencies[i] * 3

        # note this python implementation will not go out of range
        
        return total_keypresses

        '''
        Pop from counter with largest descent until 9 and increment key presses, then pops until 18 and increment 2 key presses, then pop until 27 with 3 key presses

      

        for word in list(ArtofWarCounter):
            if word in ignore:
                del ArtofWarCounter[word]

        '''
        
        '''

        You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters. 
        You can choose which characters each button is marched to as long as:
            * All 26 lowercase English letters are mapped to.
            * Each character is mapped to by exactly 1 button
            * Each button maps to at most 3 characters

        To type the first character matched to a button, you press the button once. To type the second character, you press the button twice, and so on.

        Given a string s, return the minimum number of keypresses needed to type s using your keypad

        '''
        
        '''

        distinct,one_p, two_p, three_p = len(list(set(s))), len(s), 0, 0

        if distinct > 18:
            three_p = distinct - 18
        elif distinct > 9:
            two_p = distinct - 9
            one_p = 9

        print(one_p)
        print(two_p)
        print(three_p)

        return one_p + two_p*2 + three_p*3

        '''




    



    



