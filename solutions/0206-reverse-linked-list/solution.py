# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # handle empty list (see Case 3 dataset)
        if head is None:
            return None

        # keep reference to deepest (only to fullfill test), reverseList is called with 1, test expects to return with 5
        deepest: Optional[ListNode] = None

        if hasattr(head, "next") and head.next is not None:
            deepest = self.reverseList(head.next)

            print("Reached %d, switching child %d to %d" % (head.val, head.next.val, head.val))
            head.next.next = head
        else:
            print("Reached %d, deepest" % (head.val))
            return head

        head.next = None

        return deepest
