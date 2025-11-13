'''
Problem: Find a duplicate number
Input: integer array containing n+1 integers, in range [1,n]
Output: Return the repeated number
NOTE: There is only 1 repeated number
NOTE: We cannot modify the original array

Edge Cases:
    1. empty array ---> in range [1,n]
    2. non - integers
    3. range of n in [32 bit -2billion, 2billion]
    4. non-unique, multiple answers

Method 1. 
    - Brute Force solution: For loops
    - Runtime: O(n**2)
    - Space: O(1)

Method 2. 
    - Sort + single iteration
    - Runtime: O(nlogn)
    - Space: O(1)

Method 3.
    - Single Linear Search
    - Runtime: O(n)
    - Space: O(n)

Method 4. (Modifying original array with marker)
    - Singe len == n+1, in range [1, n], find index, and mark negative val as seen
    - runtime: O(n)
    - Space: O(1)

Method 5. 
    - Binary Exclusion (Compare mid index with count of integers less than mid)
    - Runtime: O(logn)
    - Space: O(1)

Method 6.
    - Linked List Emulation
    - Given characterstics of arr of size n + 1, in [1, n]
    - Treat array as mapping of linked nodes {index: nums[i]}
    - Given guaranteed repeated number, largest number is n, and size n+1, then slow/fast. 
    - Runtime: O(n)
    - Space: O(1)
'''

class Solution:

    def findDuplicate(self, nums: list[int]) -> int:
        ''' M1. Brute force '''
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return i

    def findDuplicate(self, nums: list[int]) -> int:
        ''' M2. Sort + Single Iteration '''
        tmp = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def findDuplicate(self, nums: list[int]) -> int:
        ''' M3. Linear Search + Set '''
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

    def findDuplicate(self, nums: list[int]) -> int:
        ''' Method 4. (Modifying original array with marker)'''
        for num in nums:
            spot = abs(num) - 1
            if nums[spot] < 0:
                return abs(num)
            nums[spot] = -nums[spot]



    def findDuplicate(self, nums: List[int]) -> int:
        ''' M5. Binary Exclusion '''
        low, high = 0, len(nums) - 1
        while low < high:
            count = 0
            mid = (low + high) // 2
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low 

    def findDuplicate(self, nums: list[int]) -> int:
        ''' M6. Linked List Emulation '''
        slow, fast = nums[0], nums[0]
        # guaranteed a loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # find the beginning of loop
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

