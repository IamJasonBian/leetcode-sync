class Solution:
   def lastStoneWeight(self, stones: List[int]) -> int:
        # Iterate through and sort all the stones
        de = stones

        while len(de) > 1:
            de.sort()
            
            h1=max(de)
            de.pop()

            h2=max(de)
            de.pop()

            #print("h1:" + str(h1))
            #print("h2:" + str(h2))

            if h1 < h2:
                h2 = h2 - h1
                de.append(h2)

            elif h2 < h1:
                h1 = h1 - h2
                de.append(h1)
        
        if len(de) == 0:
            return 0
        return de[0]
