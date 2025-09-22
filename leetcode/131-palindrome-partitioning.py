class Solution:


    def palindrome(self, s, i, j):
        ''' Given string and (left, right) -> check if palindrome '''
        left = i
        right = j

        while left <= j:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False 
        
        return True 
    def partition(self, s: str) -> List[List[str]]:
        '''
        Backtracking (Include, exclude)
        '''
        res = []
        def dfs(path, i):
            if i >= len(s):
                res.append(path)
                return 
            for j in range(i, len(s)):
                # if the start (include) to index j (next include) is palindrome, try partition
                if self.palindrome(s, i, j):
                    # dfs (path + current partition [i: j+1], next index is j + 1)
                    dfs(path + [s[i:j+1]], j + 1)
        dfs([], 0)
        return res 
        
    @cache
    def partition(self, s):
        if not s: return [[]]
        res = []
        for i in range(1, len(s)  + 1):
            if s[:i] == s[:i][::-1]:
                for suffix in self.partition(s[i:]):
                    res.append([s[:i]] + suffix)
        return res 
