"""
Title: 35_search_insert_position
Given a sorted array of distinct integers and a target value, return the
index if the target is found. If not, return the index where it would be 
if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary searchinging non-recursive with loop
        # left and right pointers start at 0, -1
        # while l < r, we set the mid point and compare
        # continue the loop with the side that contains the target
        # if the target is not in the array, the left pointer is position in which to insert
        l, r = 0, len(nums) -1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid-1
        return l

        