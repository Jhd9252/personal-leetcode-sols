# -*- coding: utf-8 -*-
"""
Given an integer array 'nums', return True if any value appears at least twice
in the array. Return False if every every element is distinct.
"""
class Solution:
    ''' 
    Input: int arr nums
    Process: Determine if there is a duplicate
    Output: Boolean value if exists duplicate
    Exceptions: empty arr input, elements other than int
    Intuition (DAO):
    (1) Iterate through input 
        (A) Record past elements and compare each time
        (B) Difference between dupe and not is length of set
        (C) Use a dict for fast check
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        RT O(n**2), Space O(1)
        Brute force with nested for loops
        '''
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False 

    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        RT: O(nlogn), Space O(n)
        Sorted Approached
        '''
        sorted_arr = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i-i] == nums[i]:
                return True
        return False 

    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        RT O(n), Space O(n)
        Create a full length set() 
        Compare the lengths of each in O(1) time. 
        '''
        return len(set(nums)) != len(nums)

    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        RT O(n), Space O(n)
        Create a iterative set()
        Check lookup in O(1) time because set() implemented with hashmap in java and python
        Faster than above
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False 

    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        RT O(n), Space O(n)
        Use a full length hashmap
        Check each value occurence 
        '''
        tmp = collections.Counter(nums)
        return not all(x[1] <=1 for x in tmp.items())

    
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        RT O(n), Space O(n)
        Iterative hashmap building
        Check each iteration with early return
        Faster than above
        '''    
        tmp = {}
        for num in nums:
            if num in tmp and tmp[num] == 1: return True
            tmp[num] = 1
        return False 