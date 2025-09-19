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
        # create a bucket that has at most n-buckets or freq
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
        HashMap:
        Runtime: O(nlogn) = O(n) freq + O(nlogn) sort
        Space: O(n)
        '''
        freq = collections.Counter(nums)
        sorted_items = [x for x in sorted(freq.items(), key = lambda x: x[1])]
        return [x[0] for x in sorted(freq.items(), key = lambda x: x[1], reverse=True)][:k]
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        MaxHeap
        Runtime: O(n) count + O(n) heapify + O(logn) return k
        Space: O(2n)
        '''
        # get { num : counts }
        freq = collections.Counter(nums)
        # build an array for heap
        max_heap = [(-val, key) for key, val in freq.items()]
        # build heap from array
        heapq.heapify(max_heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        MaxHeap OPtimization
        runtime: O(n) count + O(k) push + O(logk) return = O(n)
        Space: O(k)
        '''
        freq: dict = collections.Counter(nums)
        maxHeap = []

        for key, count in freq.items():
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-count, key))
            else:
                if count > -maxHeap[0]:
                    heapq.heapreplace(maxHeap, (-count, key))
        
        return [-item[1] for item in maxHeap]

    

    


        