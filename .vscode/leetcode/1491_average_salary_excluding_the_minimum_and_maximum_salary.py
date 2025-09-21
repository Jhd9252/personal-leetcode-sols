# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:25:19 2022

@author: jhd9252

LeetCode Problem: 1491. Average Salary Excluding the Minimum and Maximum Salary
Test Cases: 43/43 passed
Runtime: 34 ms (beats 79.89% of python submissions)
Memory Usage: 13.8 MB (beats 96.42% of python3 submissions)


You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Constraints:
   3 <= salary.length <= 100
    1000 <= salary[i] <= 106
    All the integers of salary are unique.
"""

class Solution:
    def average(self, salary) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) -2)