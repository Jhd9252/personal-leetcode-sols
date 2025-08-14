'''
LeetCode 122. Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Hints:

1. Don't over think it.
2. Find local minima and maxima.
3. Calculate profit at each step.
4. The upward trend between the most optimal points, is the same as summing up the differences per day on that trend. 

For instance [1,2,3,4,5]
the profit would be 4 because buy at 1, sell at 5. 
This is the same as buying at 1, selling at 2. 
Buying at 2, selling at 3.
Buying at 3, selling at 4.
Buying at 4, selling at 5. 

'''

# Runs in O(n)
# Space is O(1) 

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total = 0 
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total 