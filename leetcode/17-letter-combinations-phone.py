class Solution:
    '''
    Given a string containing digits from 2-9 inclusive. 
    Return all possible letter combinations, in any order. 
    
    Iterate through each number in string. 
    Iterate through all possible letters.
    Once we reach the end of string, we backtrack. 
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapper = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'], 
            '9': ['w','x','y','z']
        }

        res = []

        def dfs(path, i):
            # base case: reached end of digit string
            if i >= len(digits):
                res.append(''.join(path)) # local and copied
                return

            # other wise, keep iterating over current input
            # for this index in digits string, at this level
            # we consider choosing all letters
            for letter in mapper[digits[i]]:
                # the next depth down, we move index
                # and consider all possible at that index
                dfs(path + [letter], i + 1)
                # since using local path/ stack var, implicitly popped()
        
        dfs([], 0)
        return res 



        