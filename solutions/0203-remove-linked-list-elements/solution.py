class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Handle cases where the head needs to be removed
        while head and head.val == val:
            head = head.next
        
        if not head:
            return None
        
        current = head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
