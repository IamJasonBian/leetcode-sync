# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       #for i in list node
       #store into set, 
       #de dup set
       #rebuild linked list from set

       #traverse linked list
       #push into queue, check if queue exists
       #rebuild from queue

       #traverse linked list
       #push into queue, check if queue exists (dict)
       #self.next = self.next.next
       #move again O(n)

       #return 0 if nothing in list
       
       #queue = Dict{}
       if not head:
         return
       
       #Tip of our head
       temp = head


       while head.next:
         #Try dictionary implementation
         #qe[''] = head.nextueu


         if head.val == head.next.val:
            head.next = head.next.next

         else:
            head = head.next
    
       return temp





       


