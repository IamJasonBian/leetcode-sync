class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Calculate h-index using binary search for ascending sorted citations array.
        Time: O(log n) from binary search
        Space: O(1) using only pointers
        
        Args:
            citations: List[int], sorted in ascending order
            
        Returns:
            int: h-index value
        """
        n = len(citations)
        if n == 0 or citations[n-1] == 0:
            return 0
            
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            papers_with_at_least = n - mid
            
            if citations[mid] >= papers_with_at_least:
                right = mid - 1  # try to find larger h-index to the left
            else:
                left = mid + 1   # search right half for larger citations
        
        return n - left
