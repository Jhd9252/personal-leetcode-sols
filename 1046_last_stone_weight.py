# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:17:05 2022

@author: AMDPower
"""

"""
LeetCode Problem: 1046 Last Stone Weight
Test Cases: 70/70 passed
Runtime: 23 ms (beats 67.21% of python submissions)
Memory Usage: 13.5 MB (beats 25.03% of python submissions)


You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Constraints:
    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        MaxHeap
        RT: O(n*logn)
        Space: O(n)
        '''
        for i, stone in enumerate(stones): stones[i] = -stone
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            z = abs(x-y)
            if z > 0:
                heapq.heappush(stones, -z)
        if len(stones) == 1: return -stones[0]
        return 0