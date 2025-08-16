'''
22. Generate Parentheses

Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def builder(stack, left, right):
            # base case where left and right numbers == n
            if left == right == n:
                res.append(''.join(stack))
            
            # otherwise we need to recurse deeper
            # first by adding left parenthesis
            if left < n:
                stack.append('(')
                builder(stack, left + 1, right)
                # after exhausting left limit, pop
                stack.pop()

            # if left is filled, or exhausted, add right
            if right < left:
                stack.append(')')
                builder(stack, left, right + 1)
                # after right is exhausted, pop
                stack.pop()
                
        builder(stack, 0, 0)
        return res 
            
