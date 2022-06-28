# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:51:48 2022

@author: jhd9252
Title: 347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Constraints:
    1 <= nums.length <= 105
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.
"""

class Solution:
    def topKFrequent(self, nums, k):
        # simple force solution
        d = {}
        for num in nums:
            if num in d.keys():
                d[num] += 1
            else:
                d[num] = 1
        res = []
        for idx in range(k):
            res.append(max(d, key=d.get))
            d.pop(max(d, key=d.get))
        return res
    
        # one liner
        # counter(iter).most_common(k) returns most common k nums in tuples
        # it returns k:v, therefore we take the [0] first element of each tuple
        # return as list
        # return list(zip(*collections.Counter(nums).most_common(k))))[0]
        

