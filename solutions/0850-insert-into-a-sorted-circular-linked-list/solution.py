class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode

        print(head.val)
        prev, curr = head, head.next
        toInsert = False

        while True:

            '''

                [1]: Check prev.val <= insertVal <= curr.val to mock the toInsert = True
                [2]: If toInsert is bounded, prev.next = Node(insertVal, curr)
                    

            '''

            if prev.val <= insertVal <= curr.val:
                toInsert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next
            if prev == head:
                break
        prev.next = Node(insertVal, curr)
        return head
