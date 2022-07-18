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
	 