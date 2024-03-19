class TrieNode:    
 
    #Constructor, Time O(1), Space O(1), 128 is constant
    def __init__(self, c):
        self.children = [None]*128 #don't use 26 if there is space or other special characters
        self.isEnd = False
        self.data = c


class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch)
            if not node.children[idx]:
                node.children[idx] = TrieNode(ch)
            node = node.children[idx]
        node.isEnd = True

    #returns all words with given prefix
    #Time O(n), Space O(n), n is number of nodes included(prefix and branches) 
    def startsWith(self, prefix):
        node = self.root
        res = []
        for ch in prefix:
            node = node.children[ord(ch)]
            if node == None:
                return []     
        self.helper(node, res, prefix[:-1]) 
        return res   

    def search(self, word) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch)
            if not node.children[idx]:
                return False # Corrected to use 'False'
            node = node.children[idx]
        return node.isEnd # Corrected indentation

    #recursion function called by autocomplete, Time O(n), Space O(n)	
    # n is number of nodes in bra
    def helper(self, node, res, prefix):
        if node == None:
            return
        if node.isEnd :
            res.append(prefix + node.data)		   	      	   
        for child in node.children:	         
            self.helper(child, res,prefix + node.data)		             
 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
