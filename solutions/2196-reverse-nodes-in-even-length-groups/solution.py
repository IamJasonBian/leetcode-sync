class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, node = 0, head
        while node: n, node = n+1, node.next
        
        k, node = 0, head 
        while n: 
            k += 1
            size = min(k, n)
            stack = []
            if not size & 1: 
                temp = node 
                for _ in range(size): 
                    stack.append(temp.val)
                    temp = temp.next 
            for _ in range(size): 
                if stack: node.val = stack.pop()
                node = node.next 
            n -= size
        return head 
