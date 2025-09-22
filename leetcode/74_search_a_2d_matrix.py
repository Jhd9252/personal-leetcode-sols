'''
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
from functools import reduce
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int): 
        '''
        Brute Force: Linear Search 
        RT: O(nm)
        Space: O(1)
        '''
        for row in matrix:
            for num in row:
                if num == target:
                    return True
        return False 

    def searchMatrix(self, matrix: List[List[int]], target: int): 
        '''
        Use row start and end points
        RT: O(n + m)
        Space: O(1)
        '''
        for row in matrix:
            if row[0] <= target and target <= row[-1]:
                for num in row:
                    if num == target:
                        return True
        return False 

    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Binary Search: Flatten the matrix
        (1) Each row is sorted
        (2) No row overlaps over another. 
        RT: O(log(n+m))
        Space: O(1)
        '''
        n = len(matrix)
        m = len(matrix[0])
        matrix = reduce(lambda x,y: x + y, matrix)
        l, r = 0, n*m-1
        while l <= r:
            m = (l + r) // 2
            if matrix[m] == target:
                return True
            elif matrix[m] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False 

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Binary Search:
        (1) Intuition: Since we have n-rows and m-cols, then a number is (rowID * m) + left over
        RT: O(log(nm))
        Space: O(1)
        ''' 
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n*m-1
        while l <= r:
            mid = (l+r) // 2
            num = matrix[mid // m][mid % m ]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False 

