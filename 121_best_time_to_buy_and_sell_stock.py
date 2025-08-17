# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 22:23:31 2022

@author: jhd9252

Title: 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Notes:
We can only choose 1 day to buy and 1 day to sell.
Thus, we need to track the lowest cost to the left of our position. 
Thus, we need to track the highest cost to the right of our position. 

The max profit the smallest we've tracked so far, along with a tracker of curr-smallest
Thus, the tagged lowest price may not move as we iterate and get current prices. 
This satifies the temporal property of buying and selling. 
"""


    
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        '''
        Brute Force: Two for loops to find the highest day greater than current price. 
        runtime: O(n**2)
        space: O(1)
        '''
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        '''
        One pass solution:
        Track the lowest price seen so far and the max profit that can be made with that price
        Runtime: O(n)
        Space = O(1)
        '''
        low = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit, price - low)
            low = min(low, price)
        return profit
        
prices = [7,1,5,3,6,4]
a = Solution()
b = a.maxProfit(prices)
        
