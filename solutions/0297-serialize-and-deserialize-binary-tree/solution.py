# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        arr = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            arr.append(str(node.val) if node else " ")
            if not node:
                continue
            q.append(node.left)
            q.append(node.right)
        while arr and arr[-1] == " ":
            arr.pop()
        
        return ",".join(map(str, arr))

    def deserialize(self, data):
        data = data.split(',')
        if data == ['']:
            return None
        res = [None if i == ' ' else int(i) for i in data]
        return res


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))                     
