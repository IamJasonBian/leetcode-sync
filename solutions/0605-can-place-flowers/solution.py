class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        
        '''

            You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots. 

            Given an integer array flowerbed containing 0s and 1s, where 0 means empty and 1 means not empty, and an integer n, 
                return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rules and false otherwise.


            Invalid: two adjacent

            Steps:

                1. Find sequence of alternating 0s and 1s, I.E. "Slots"
                2. For "Slots" found, add in the flowers
                3. Pre-defined intos we know beds can't be sequential:
                    So it is either 1 0 1 0 ...
                        or 1 0 0 .... 0 1 etc
                            in the 1 0 0 0 1 case
                                we can put a 1 
                                    in the 1 0 0 1 case
                                        we can't put any flowers
                                            so only 1 0 1 or 
                                                1 0 0 0 1 etc
                                                    can be used
                                                        for 1 0 0 0 0 1
                                                            this is 1 as well so it's really the total count of 3 or 5 slots
                                                                1 0 1 0 1 0 1


                                            Consecutive zeros doesn't work because:

                                            After planting a flower, the next valid spot isn't always 2 positions away.
                                                Example: In [0,0,0,0,0], planting at index 2 leaves [0,0,1,0,0] where you can still plant at index 0.

        '''


        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1  # We do need to plant to run the above scan vs generalizing via zeros
                n -= 1
            if n <= 0:
                return True
        return n <= 0
