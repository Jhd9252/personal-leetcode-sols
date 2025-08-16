'''
84. Largest Rectangle in Histogram

Hard


Given an array of integers heights representing the histogram's 
bar height where the width of each bar is 1, return the area of 
the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.


Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Brute Force: 
        (1) For each index, track current minimum
        (2) calculate the max area possible, note that each bar has width of 1
            - consider j starting at i
        (3) update overall max
        RT: O(n^2)
        Space: O(1)
        '''
        res = 0
        n = len(heights)
        for i in range(n):
            low = heights[i]
            for j in range(i, n):
                low = min(low, heights[j])
                res = max(res, low * (j-i+1))
        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Monotonic Increasing Stack:
        (1) We see that each higher bar adds area
        (2) We also see that a lower bar limits the area
            - Adding a lower bar adds at most 1 width. While, also lowering the min height. 
        (3) Add a bar when larger. If lower, then we start popping the stack and calculating backwards. 
        Idea:
        (1) We start calculating the area starting with single bar itself, then moving forward. 
        '''
        # exceptions
        if not heights: return 0
        maxArea = 0
        stack = []
        heights.append(0)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][-1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        return maxArea 
