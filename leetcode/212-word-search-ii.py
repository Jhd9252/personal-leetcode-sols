'''
212. Word Search II

Hard

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent 
cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False 

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
    
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def dfs(self, board, r, c, n, m, node, word, visited, res):

        # check if cell is valid + if char is possible in word chain + not visited
        if (r < 0 or r >= n or c < 0  or c >= m or 
            board[r][c] not in node.children or (r,c) in visited):
            return 

        # process this node to ensure no repeated uses
        visited.add((r,c))

        # move onto next node in word chain
        node = node.children[board[r][c]]

        # add the current valid char onto stack
        # NOTE: strings are immutable, so each recursive call has its own copy
        # NOTE: when dfs is returned (word not found / found), the current string is discarded
        word += board[r][c]

        # if the current node is END -> add word to result 
        if node.end: res.add(word)

        # recursively check four cardinal directions
        self.dfs(board, r - 1, c, n, m, node, word, visited, res)
        self.dfs(board, r + 1, c, n, m, node, word, visited, res)
        self.dfs(board, r, c + 1, n, m, node, word, visited, res)
        self.dfs(board, r, c - 1, n, m, node, word, visited, res)

        # once we reach here, we exhausted everything, backtrack and pop off cell
        # NOTE: Visited is a set(), which is mutable, meaning it needs to be explicitly cleared
        visited.remove((r,c))
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # first, add all the target words into our prefix tree
        for w in words:
            self.root.addWord(w)

        # get measurements
        ROWS, COLS = len(board), len(board[0])

        # get aux variables to ensure no repeat words, infinite loops or repeated chars
        res, visited = set(), set()

        # call dfs on each cell
        for r in range(ROWS):
            for c in range(COLS):
                self.dfs(board, r, c, ROWS, COLS, self.root, "", visited, res)
        # return a list of words found
        return list(res)


        