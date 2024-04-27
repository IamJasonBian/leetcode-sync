class Solution:
    def countNodes(self, root, l=1, r=1):
        
        '''
        This makes way more sense than the other complicated traversal lol:
        
        '''

        if not root : return 0
        
        left = right = root                           # compute both left and right heights of
        while left  := left.left   : l += 1           # each subtree by going all way down to
        while right := right.right : r += 1           # the left and right (in logN time)

        if l == r : return 2**l - 1                   # if it's a full tree, its size is known
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    
