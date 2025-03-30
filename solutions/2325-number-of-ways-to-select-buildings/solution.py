class Solution:
    def numberOfWays(self, s: str) -> int:



        '''
            **Constraint:** 
                * no two consecutive buildings out of the selected buildings can be of the same type

            Some factors:

            001101 is allowed but not 011 

                * We need to select three buildings so only 010 or 101 are possible buildings
                * How do we construct those two patterns from smaller patterns? 
                    * The answer is selection:
                        in [001101, 001101, and 001101 
                                We are selecting 0 first
                                Selection starts with a value and then propogates to the other values
                                    * How does Propogation Work (I.E. criteria)

                                We look at all the 0 starts and then look at all the 1 starts
                                Two arrays, if repeat add to the other array.
                                In terms of partitioning, we can do either 01 or 10 as two options. Let n)1[i] be the number of '01' subsequences that exist in the prefix of s up to the ith building. 

        How about a pattern matching approach:
        
        '''

        # Count of each pattern seen so far
        count_0 = 0
        count_1 = 0
        count_01 = 0
        count_10 = 0
        count_010 = 0
        count_101 = 0
        
        for char in s:
            if char == '0':
                # Update pattern counts ending with '0'
                count_0 += 1
                count_10 += count_1  # Add new "10" patterns using all previous '1's
                count_010 += count_01  # Add new "010" patterns using all previous "01"s
            else:  # char == '1'
                # Update pattern counts ending with '1'
                count_1 += 1
                count_01 += count_0  # Add new "01" patterns using all previous '0's
                count_101 += count_10  # Add new "101" patterns using all previous "10"s
        
        # The answer is the total number of "010" and "101" patterns
        return count_010 + count_101





        



