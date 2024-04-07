class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        # Initialize two pointers as headA and headB.
        pointerA, pointerB = headA, headB

        # Traverse through the lists.
        # If a pointer reaches the end of a list, move it to the head of the other list.
        while pointerA != pointerB:

            # We are essentially swapping at the point of intersection here
            
            pointerA = headB if pointerA is None else pointerA.next
            # Do the same for pointerB.
            pointerB = headA if pointerB is None else pointerB.next

        # If there is an intersection, pointerA and pointerB will be at the intersection node.
        # If there is no intersection, pointerA and pointerB will be at None, the end of the lists.
        return pointerA

