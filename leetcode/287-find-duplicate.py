'''
287. Find the Duplicate Number
Medium

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
'''

class Solution:
    '''
    Unsorted array [1,n] inclusive
    only one unique answer
    cannot modify the array
    only use constant extra space
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        ''' 
        Brute Force for loops 
        Runtime :O(n**2)
        Space: O(1)
        Not constant or O(n) time
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return i
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Sorting in place, traverse once
        RT: O(nlogn)
        Space: O(1)
        Not allowed due to modifying array
        '''
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def findDuplicate(self, nums: List[int]) -> int:
        ''' 
        Naive Brute Force with set
        Runtime: O(n)
        Space: O(n)
        Not allowed because of extra space
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Marked visited value with its negative
        (1) all values are in range [1, n]
        (2) Size is n+1
        (3) which means each num is mapped to an index, use it as a check
        (4) we compare abs(value) with its index to check negative
        Runtime: O(n)
        Space: O(1)
        Not allowed due to modifying the array
        '''
        for num in nums:
            spot = abs(num) - 1
            if nums[spot] < 0:
                return abs(num)
            nums[spot] = -nums[spot]

    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Binary Search with convergence
        (1) count how many elements greater than mid
        (2) if count > mid, then repeated element on [left, mid]
        RT: O(nlogn)
        Space: O(1)
        '''
        low, high = 1, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low 

    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Given characteristics of array of size n+1 with i in [1, n]
        Then, we can treat it as a linked list, where each {index: nums[n]}
        So if array [1,3,4,2]
        Then we travel as 0->1->3->2->4->null
        So if array with repeat [1,3,4,2,2]
        then we travel as 0->1->3->2->4->2->4->2...repeat
        Thus, if we use slow, fast, eventually we will get a linked list
        RT: O(n)
        Space: O(1)
        '''
        slow, fast = nums[0], nums[0]
        # find the cycle (this is not the start point or dupe num)
        # slow moves 1, fast moves 2 = eventually cycle
        # dont use while slow != fast because they start the same
        while True:  # or nums[nums[fast]]
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # finally, slow restarts, fast stays put
        # now both move at speed of 1
        # according to floyd algorithm, they will meet at the start 
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow 
        