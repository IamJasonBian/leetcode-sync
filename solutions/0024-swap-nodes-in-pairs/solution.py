# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
        We are swap p2.next and p2 at each step, 
        We use p1 to keep track of the prev node of p2, since the prev node needs to link to the swapped node
        
        stop condition:
            We need to make sure p2 is not none for p2.next to work && p2.next is not None for assignment of `p2.next.next`
            Actually when num nodes is even e.g. 1 -> 2 -> 3 -> 4, `p2 is None` will be the stop condition
            when num nodes is odd e.g. 1 -> 2 -> 3, `p2.next is None` will be the stop condition.
    """
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p1, p2 = dummy, head
        
        while p2 and p2.next:
            # swap
            p1.next = p2.next
            p2.next = p2.next.next
            p1.next.next = p2
            
            # iter forward
            p1 = p2
            p2 = p2.next
        
        return dummy.next
