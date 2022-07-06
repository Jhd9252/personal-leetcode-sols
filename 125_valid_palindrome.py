# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 20:02:34 2022

@author: jhd9252

Title: 125. valid palindrome

After converting into lowercase letters, removing all non-alphanumeric characters, return whether the string is a palindrome or not. 


Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


# Purpose is to determine if the entire converted string is a palindrome
# Therefore, we can simply convert and return comparison of string
# read forwards and backwards
class Solution:
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s==s[::-1]
    
    