

# this is a backtracking algorithm
# using for all choices, for all steps with condition

def generateParenthesis(n: int):
    '''
    Given n-int for n-pairs, generate all possible well-formed combinations
    Well formed if ...
    n is a valid int between ....
    Methods: Backtracking, recursion, DFS
    '''
    res = []
    stack = []

    def backtrack(res, stack, n, left, right):
        # base case
        if left == right == n:
            res.append(''.join(stack))
            return res
        
        # conditional answer modification
        if left < n:
            backtrack(res, stack + ['('], n, left + 1, right)
        if right < left:
            backtrack(res, stack + [')'], n, left, right + 1)
        
        return res

