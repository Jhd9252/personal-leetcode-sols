# -*- coding: utf-8 -*-
"""
Created on Sun May 22 02:58:16 2022

LeetCode Problem: 174. Dungeon Game
TestCases: 45 / 45 test cases passed.
Runtime: 79 ms (runtime beats 87.26 % of python3 submissions)
Memory Usage: 15.2 MB 9beats 50.14 % of python3 submissions

Given a 2D array, representing a dungeon layout (m by n)
Each square (including the beginning square is either a health pot, or a curse)
You start at the top-left square
The princess resides at the bottom-right square
If your HP reaches zero, you die.
Find the minimum initial health needed to rescue the princess. 


Constraints:
    1. m == dungeon.length
    2. n == dungeon[i].length
    3. 1<= m, n <= 200
    4. -1000 <= dungeon[i][j] <= 1000
    
    
Traversing from bottom-right to top-left, we calculate how much hp is required to reach the princess from the current cell.

The first step is to calculate how much hp is required to save the princess upon reaching dungeon[m-1][n-1]:
dungeon[i][j] = min(dungeon[i][j], 0) * -1 + 1
For example:
If dungeon[m-1][n-1] == -5, then we need 6 hp.
If dungeon[m-1][n-1] >= 0 then we only need 1 hp.

"""

def calculateMinimumHP(self, dungeon):
    # m is the number of rows
    # n is the number of columns 
    m, n = len(dungeon), len(dungeon[0])
    
    # iterate through all the rows backwards
    for i in range(m-1, -1, -1):
        
        # iterate through all the cols backwards for each row
        for j in range(n-1, -1, -1):
            
            # if the current position is the bottom right (princess)
            # take the minimum between (current position, 0) with formula to take the positive + 1
            # this ensures that if princess square is -1, we determine that we need 2 health to survive.
            if i == m-1 and j == n-1:
                    dungeon[i][j] = min(dungeon[i][j], 0) * -1 + 1
                    
            # if the current position is in the last row
            elif i == m-1:
                
                # set the current position number to the max(next pos in row, 1)
                dungeon[i][j] = max(dungeon[i][j+1] - dungeon[i][j], 1)
                
            # if the current position is in the last column
            elif j == n-1:
                
                # set current position number to max(next row, 1)
                dungeon[i][j] = max(dungeon[i+1][j] - dungeon[i][j], 1)
                
            # if current position is not in last row/col
            else:
                
                # set the current position number to max(min(next row,next col) - current position, 1)
                dungeon[i][j] = max(min(dungeon[i][j+1], dungeon[i+1][j]) - dungeon[i][j], 1)
                
    # therefore once we reach the beginning square, we have the minimum health required
    return dungeon[0][0]
    
