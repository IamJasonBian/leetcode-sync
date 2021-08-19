# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def list_to_link(lst):

            if len(lst) == 1:
                return ListNode(lst[0])
            return ListNode(lst[0], list_to_link(lst[1:]))  # <<<< RECURSIVE

        #Parse two numbers from Linked List
        l1_list = []
        l2_list = []
        final = 0
        
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
            
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        
        base = 1
        for i in range(len(l1_list)):
            
            final = final + int(l1_list[i]*base)
            base = base*10
        
        base = 1
        for i in range(len(l2_list)):
            
            final = final + int(l2_list[i]*base)
            base = base*10
            
        final_ls = [int(x) for x in str(final)[::-1]]
            
        init_flag = 0
        
        final_ll = list_to_link(final_ls)
        
        
        print(final_ll)
        return(final_ll)

