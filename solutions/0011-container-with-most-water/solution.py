class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1 
        H = 0

        while l != r:
            
            length = r - l 
            tmp = min(height[l], height[r])*(r-l)

            print("run")
            print(min(height[l], height[r]))
            print(r-l)
            print(tmp)

            if H < tmp:
                H = tmp


            if height[l] <= height[r]:
                l = l + 1
            else:
                r = r - 1

        return H
