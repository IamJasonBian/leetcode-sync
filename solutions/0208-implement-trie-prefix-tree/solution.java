class Trie {
    class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isEndOfWord = false;
    }

    TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode crawler = root;
        for (var c : word.toCharArray()) {
            if (!crawler.children.containsKey(c)) {
                crawler.children.put(c, new TrieNode());
            }
            
            crawler = crawler.children.get(c);
        }

        crawler.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNode crawler = root;
        for (var c : word.toCharArray()) {
            if (!crawler.children.containsKey(c))
                return false;
            
            crawler = crawler.children.get(c);
        }

        return crawler.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode crawler = root;
        for (var c : prefix.toCharArray()) {
            if (!crawler.children.containsKey(c))
                return false;
            
            crawler = crawler.children.get(c);
        }

        return true;   
    }
}


