'''
211. Design Add and Search Words Data Structure

Medium

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure 
that matches word or false otherwise. word may contain dots '.' where dots 
can be matched with any letter.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True
    
    def search(self, word: str) -> bool:
        ''' Use DFS '''
        return self._dfs(self.root, 0, word)
    
    def _dfs(self, node, i, word):
        # base case (ptr reaches past end of word)
        # all chars have matched so far -> check is end
        if i == len(word): return node.end

        # on recursion down, check if wild marker
        if word[i] == '.':
            # If YES, DFS on all children, skipping this index char
            for child in node.children:
                if self._dfs(node.children[child], i + 1, word):
                    # if reach end of word and END, carry up TRUE
                    return True
        # on recursion down, if not wild marker
        if word[i] in node.children:
            # continue recursion (if past, and END-> TRUE, else FALSE)
            return self._dfs(node.children[word[i]], i+1, word)
        # else not past word, not wild marker, not match, its a mismatch
        return False 
    



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)