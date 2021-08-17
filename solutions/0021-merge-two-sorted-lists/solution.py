# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      

        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
        
        lists = [l1, l2]
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put(Wrapper(l))
        while not q.empty():
            node = q.get().node
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put(Wrapper(node))
        return head.next
