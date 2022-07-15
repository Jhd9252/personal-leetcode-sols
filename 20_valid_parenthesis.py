"""
Title: 20_valid_parenthesis
Given a string containing only parenthesis, curly brackets and straight brackets, determine
if the input string is valid.
Input string is valid if open brackets must be closed by the same type of brackets
Open brackets must be closed the correct order.
"""
class Solution:
    def isValid(self, s: str) -> bool:
		# creating a dictionary to hold bracket types as pairs
    	# creating a stack (LIFO)
    	# for each character in string
    	# check if its a left bracket -> append to stack
    	# else if the stack is empty (no macthing to left bracket) or left bracket doesn't match pop()-> False
    	# Last, check that stack as no unmatached left brackets. 

    	d = {'(':')', '{':'}','[':']'}
    	stack = [] # as array. LIFO or first in first out
    	for char in s:
    		if char in d:
    			stack.append(char)
    		elif len(stack) == 0 or d[stack.pop()] != char:
    			return False
    	return len(stack) == 0

