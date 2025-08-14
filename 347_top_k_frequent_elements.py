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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''' 
        Hashmap {num: occur} -> Sorting on key -> Return 
        RT: O(nlogn)
        - counter goes through O(n)
        - sorting is O(nlogn)
        Space: O(n)
        '''
        count = collections.Counter(nums)
        return [x[0] for x in sorted(count.items(), key= lambda x:x[1], reverse=True)][:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        HashMap {num: occur} -> Using MinHeap for K-elements -> Return 
        RT: O(nlogk)
        Space: O(n)
        '''
        count = collections.Counter(nums)
        minheap = []

        for key, count in count.items():
            if len(minheap) == k:
                heapq.heappushpop(minheap, (count, key))
            else:
                heapq.heappush(minheap, (count, key))
        
        return [item[1] for item in minheap]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        HashMap with bucket sort
        RT: O(n)
        Space: O(n)
        '''
        # get the num, freq
        counter = collections.Counter(nums)
        n = len(nums)
        # create a bucket that has at most n-buckets
        bucket = [[] for i in range(n+1)]

        # place the num in the bucket according to freq
        for num, freq in counter.items():
            bucket[freq].append(num)

        # iterate backwards, extracting each num and decrementing k
        ans = []
        for bucketIdx in range(n, 0, -1):
            for num in bucket[bucketIdx]:
                if k == 0:
                    break
                ans.append(num)
                k -= 1
        return ans 

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''' 
        Hashmap {num: occur} -> Sorting on key -> Return 
        RT: O(nlogn)
        - counter goes through O(n)
        - sorting is O(nlogn)
        Space: O(n)
        Note: Given max length of array nums, this O(logn) algorithm might be the fastest. 
        '''
        count = collections.Counter(nums)
        return [x[0] for x in sorted(count.items(), key= lambda x:x[1], reverse=True)][:k]
