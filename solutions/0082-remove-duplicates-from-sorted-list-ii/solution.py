class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        # most challenging situation: the list head is to be removed
        if not head: return head
        
        if not head.next: return head


        if head.val != head.next.val:

            # check head and the immediate value ahead of head 
            head.next = self.deleteDuplicates(head.next)

            return head


        if not head.next.next or head.next.val != head.next.next.val:


            return self.deleteDuplicates(head.next.next)

        return self.deleteDuplicates(head.next)
