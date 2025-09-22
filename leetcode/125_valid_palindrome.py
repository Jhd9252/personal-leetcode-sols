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


class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Brute Force: Clean, reverse and compare
        Runtime: O(n) 
        - cleaning takes O(n)
        - Reverse takes O(n)
        - compare O(n)
        Space: O(n) for extra cleaned space 
        '''
        clean = [x.lower() for x in s if x.isalnum()]
        return clean == clean[::-1]

    def isPalindrome(self, s:str) -> bool:
        """
        Optimize: Create a clean string, two pointer solution
        Runningtime: O(n) + O(n//2) = O(n)
        Memory: O(n)
        """
        tmp = [char.lower() for char in s if char.isalnum()]
        return all(tmp[idx] == tmp[~idx] for idx in range(len(tmp)//2))

    def isPalindrome(self, s: str) -> bool:
        '''
        Two pointer approach
        RT: O(n)
        Space: O(1) 
        '''
        l, r = 0, len(s) - 1
        while l <= r:
            # loop left until valid char
            if not s[l].isalnum(): 
                l += 1
                continue
            # loop right until valid char 
            if not s[r].isalnum():
                r -= 1
                continue
            # both left and right valid char
            if s[l].lower() != s[r].lower():
                return False 
            l += 1
            r -= 1

        return True 


        
        