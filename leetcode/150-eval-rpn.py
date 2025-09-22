'''
150. Evaluate Reverse Polish Notation

Medium

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.


Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        A Reverse Polish Notation -> Stack
        From the input, we see that:
            1. Each number is pushed onto a stack
            2. When an operator is called, do we pop the last two from stack. 
        If we are the ith stack call, we can assign (i-1) as the result. 
        This way, at the end, the first and only item on the stack is the result. 
        '''
        stack = []
        for token in tokens:
            if token not in ['+', '-', '/', '*']:
                stack.append(int(token))
            else:
                tmp = stack.pop()
                if token == '+':
                    stack[-1] += tmp
                elif token == '-':
                    stack[-1] -= tmp
                elif token == '/':
                    stack[-1] = int(stack[-1]/tmp)
                else:
                    stack[-1] *= tmp
        return stack[-1]