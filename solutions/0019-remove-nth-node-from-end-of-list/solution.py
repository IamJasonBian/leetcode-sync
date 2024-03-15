from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        '''The two-pointer approach is used in this problem to efficiently find the node that is n nodes from the end of the linked list. 
        The reason for using two pointers is to maintain a reference to the node that is n nodes behind the current node, as we traverse the list.
         This is crucial because once we reach the end of the list, we need to know which node is n nodes behind to remove the correct node.'''

        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # Move the second pointer n nodes ahead
        for _ in range(n + 1):
            second = second.next
        
        # Move both pointers until the second pointer reaches the end
        while second:
            first = first.next
            second = second.next
        
        # Remove the nth node from the end
        first.next = first.next.next
        
        # Return the new head node
        return dummy.next

