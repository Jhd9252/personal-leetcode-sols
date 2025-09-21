"""
Koko Eating Bananas

Given array of integers representing piles of bananas.
Given hours = integer.

Koko wants to eat bananas per hour such that she can eat the slowest but still finish. 

Return k = bananas per hour

Input: piles = [3,6,7,11], h = 8
Output: 4
"""
import math
class Solution:
	def minEatingSpeed(piles, h):
		# Solution 1: brute forcing linear time -> increasing k starting from 1 bananas per hour (TLE)

		# Solution 2: Linear time traversing K within bounds given
		# Since Koko at most eats 1 pile per hour, than k < max(piles) ####### max
		# Since time constraint of h=hours, than  sum(piles) / h < k ########### min

		# Solution 3: Given the [low, high] of constraints from Solution 2, we can also do binary search. 
		l, r = max(1, sum(piles) // h), max(piles)
		while l < r:
			m = (r+l) // 2
			time = sum([math.ceil(i/m) for i in piles])
			if time > h:
				l = m + 1
			else:
				r = m
		return l

	'''
	There are n-piles of bananas.
	The ith piles is piles[i]. 
	The guards will come back in h-hours.
	Koko decides bananas per hour (k).
	If pile has less than k, it takes that hour slot. 
	Return minimum integer k, so Koko can finish within h-hours. 
	'''
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		'''
		Minimum k-bananas per hour. 
		Therefore we need to start from less to higher. 
		Can we constrain k? 
		(1) We know 'k' must be at least 1. 
		(2) We know that 'k' is at most max(piles)
		(3) Then we know that 1 <= k <= max(piles)
		How do we check if a k is sufficient? 
		When the however many hours it takes <= h
		'''
		if len(piles) <= 0 or h == 0:
			return 0

    
		def check(piles, h, k):
			# ceil(pile/k) gives us how many hours it takes to eat a pile 
			# sum up the slotted hours needed
			# check if its less than or equal to h
			return sum(ceil(pile/k) for pile in piles) <= h

		# we want to find the minimum one in range[1, max(piles)]
		# use binary search, converging on the left
		left, right = 1, max(piles)
		# we are looking for the left bound
		while left < right:
			mid = (left + right) // 2
			if check(piles, h, mid):
				right = mid
			else:
				left = mid + 1 
		return right 

