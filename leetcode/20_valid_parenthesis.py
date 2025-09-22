"""
Title: 20_valid_parenthesis
Given a string containing only parenthesis, curly brackets and straight brackets, determine
if the input string is valid.
Input string is valid if open brackets must be closed by the same type of brackets
Open brackets must be closed the correct order.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        STACK (FILO): First parenthesis or bracket is the last to be closed
        RT : O(n)
        Space: O(n)
        '''
        stack = []
        chars = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        for char in s:
            if char in chars:
                stack.append(char)
            else:
                if len(stack) <=0 or char != chars[stack.pop()]:
                    return False 
        return len(stack) == 0

    def isValid(self, s: str) -> bool:
        '''
        Could potentially reduce the space to O(1) with a dedicated check function.
        But this creates an extra call stack for each bracket.
        '''
        pass

