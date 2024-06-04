class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to hold child nodes
        self.is_word = False  # Flag to mark the end of a word

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()  # Root node of the Trie

    def addWord(self, word: str) -> None:
        """
        Adds a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.dfs_search(self.root, word, 0)

    def dfs_search(self, node: TrieNode, word: str, index: int) -> bool:
        """
        Helper function to perform depth-first search on the Trie.
        """
        if index == len(word):
            return node.is_word

        if word[index] == '.':
            for child_node in node.children.values():
                if self.dfs_search(child_node, word, index + 1):
                    return True
        elif word[index] in node.children:
            return self.dfs_search(node.children[word[index]], word, index + 1)

        return False

