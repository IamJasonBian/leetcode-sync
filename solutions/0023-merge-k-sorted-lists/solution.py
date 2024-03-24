from typing import List, Optional
from heapq import heappop, heappush

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a priority queue (heap)
        heap = []
        
        # Add the head of each linked list to the heap
        for i, l in enumerate(lists):
            if l: # Check if the linked list is not empty
                heappush(heap, (l.val, i))
        
        # Initialize the head and current node of the result linked list
        dummy = ListNode(0)
        current = dummy
        
        # Pop the smallest element from the heap and add it to the result linked list
        while heap:
            val, index = heappop(heap)
            current.next = ListNode(val)
            current = current.next
            
            # Push the next element from the same linked list into the heap
            if lists[index]:
                lists[index] = lists[index].next
                if lists[index]:
                    heappush(heap, (lists[index].val, index))
        
        return dummy.next
