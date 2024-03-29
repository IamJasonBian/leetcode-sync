from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Sort the tickets based on the destination airport
        tickets.sort(key=lambda x: x[1])
        
        # Step 2: Create a graph to represent the tickets
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        
        # Step 3: DFS to find the itinerary
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop(0))
            itinerary.append(airport)
        
        itinerary = []
        dfs("JFK")
        
        # Step 4: Return the itinerary in reverse order
        return itinerary[::-1]
