class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Calculate h-index for unsorted citations array using counting sort approach.
        
        Time: O(n) by using counting/bucket sort concept
        Space: O(n) for the count array
        
        Key insight:
        - Any citation count larger than n can be counted as n
        - We can count papers for each citation level and work backwards
        """
        n = len(citations)
        
        # Create count array - index i represents i citations
        # Any citation > n can be counted as n since h-index can't exceed n
        counts = [0] * (n + 1)
        
        # Count papers for each citation number
        for cite in citations:
            if cite >= n:
                counts[n] += 1
            else:
                counts[cite] += 1
        
        # Start from the highest possible h-index (n)
        # total_papers keeps track of papers with at least i citations
        total_papers = 0
        
        # Work backwards to find highest valid h-index
        for i in range(n, -1, -1):
            total_papers += counts[i]
            if total_papers >= i:
                return i
                
        return 0
