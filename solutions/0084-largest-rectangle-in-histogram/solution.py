from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Find the largest rectangle area in a histogram.

        Args:
            heights: List of integers representing bar heights

        Returns:
            Maximum rectangular area
        """
        if not heights:
            return 0

        stack = []  # Stack to store indices
        max_area = 0

        for i, h in enumerate(heights):
            # While current height is less than stack top
            while stack and heights[stack[-1]] > h:
                # Pop and calculate area with popped height
                height_index = stack.pop()
                height = heights[height_index]
                # Width is from element after new stack top to current index
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        # Process remaining bars in stack
        while stack:
            height_index = stack.pop()
            height = heights[height_index]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area


