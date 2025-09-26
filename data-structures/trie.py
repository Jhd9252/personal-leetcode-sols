class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
    
    def search(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end
    
    def starts_with(self, prefix: str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False 
        node = node.children[char]
        return True
    
    