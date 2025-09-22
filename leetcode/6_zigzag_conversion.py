# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 18:58:15 2022

@author: jhd9252

convert a given string into a zigzag pattern (printed)
Return the resulting string read from left to right, top to bottom

Example:
    
    1---------------------> "PAYPALISHIRING"
    
    2---------------------> P   A   H   N
                            A P L S I I G
                            Y   I   R
    
    3--------------------->"PAHNAPLSIIGYIR"
"""

class Solution(object):
    def convert(self, s, numRows):
        # special case of numRows = 1 or that numRows >= len(s), return s as is. 
        if numRows == 1 or numRows >= len(s):
            return s

        # create a matrix of length numrows
        matrix = [''] * numRows
        
        # start with col = 0
        # start with row = 1 
        col, row = 0, 1

        # for every letter in the string
        for x in s:
            # set letter in position col 0, row 1
            matrix[col] += x
            # if col == 0, set row = 1 to fill in first col
            if col == 0:
                row = 1
            # if the col is the last column    
            elif col == numRows -1:
                # set row = -1, meaning go back to the top
                row = -1
            # set col += row
            col += row

        return ''.join(matrix)