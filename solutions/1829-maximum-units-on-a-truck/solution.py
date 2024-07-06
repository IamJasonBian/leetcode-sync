class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the boxes by the number of units in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        res = 0
        for boxCount, unitsPerBox in boxTypes:
            # If the current box type can fit entirely on the truck, add all its units
            if truckSize >= boxCount:
                res += boxCount * unitsPerBox
                truckSize -= boxCount
            else:
                # Otherwise, add only the portion that fits and break the loop
                res += truckSize * unitsPerBox
                break
        
        return res

