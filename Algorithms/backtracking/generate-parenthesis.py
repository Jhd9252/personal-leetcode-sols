

# this is a backtracking algorithm
# using for all choices, for all steps with condition

def generateParenthesis(n: int):
    ''' Given n-int for n-pars, generate all possible well-formed combinations'''
    res = []
    stack = []

    def backtrack(res, stack, n, left, right):

        # base case -> answer
        if left == right == n:
            res.append(''.join(stack))

        # otherwise, all choices with conditions
        if left < n:
            backtrack(res, stack + ['('], n, left + 1, right)
        
        if right < left:
            backtrack(res, stack + [')'], n, left, right + 1)

        return res 