class TrieNode:
    def __init__(self):
        self.ch = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        '''
        Inputs

            ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
            [],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]

            ["a", "b", "aa"]

        Outputs


            [null,null,null,null,false,true,true,true]
            1 <= word.length <= 25

                10^4

            L - length of word
            N - length of inputs (candidates/number of calls to make)
            M - number of search calls 
            K - return or input size   

            AddWord - Size of N (purely write) O(N)
            Query for Search - Need to iterate and find first match O(N*M)
            Space - O(N)

        Brute Force

            bad iterate until the first hit (return True) 
            dad
            mad
            pad
            pad
            pad

        Store all permuations of the inputs, and do a direct hash on the input + remaining length (validate ..) + I.E. store actual length 

            a
            b

            AddWord - take the added word and hash all permutations into a size bucket
                            * 1 <= word.length <= 25 (alot of permutations)
            Query for Search - Need to iterate and find first match O(1)

        Trie that roots on the top level word
            Sub-Nodes that track the sub character (all pre/post-fixes)

            Runtime: 
                Add/Search - O(L for Tree depth)

            Space - O(N*L)


        root
        
        b
            a

                    n
                d

                    d 
                        i
                            e
        d
            a
                d
        
        m
            a

                d
        
        p
            a
                d


        '''        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.ch.setdefault(c, TrieNode())
        node.end = True
        
    def search(self, word: str) -> bool:
        def dfs(i: int, node: TrieNode) -> bool: 
            if i == len(word):
                return node.end
            c = word[i]
            if c == '.':
                for nxt in node.ch.values():
                    if dfs(i + 1, nxt):
                        return True
                return False
            if c not in node.ch:
                return False
            return dfs(i + 1, node.ch[c])
        return dfs(0, self.root)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
