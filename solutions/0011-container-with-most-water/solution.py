class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        min_value = float('inf') 
        max_value = float('-inf')       
        i=0
        j = len(height)-1
        while i<j:
            min_value = min(height[i],height[j]) 
            max_value = max(max_value,min_value*(j-i)) #Calculate the max distance 
            if height[i]<height[j]:
                i+=1   # move the left index 
            else:
                j-=1 #move the right index 
        return max_value
