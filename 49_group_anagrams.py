# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:08:02 2022

@author: jhd9252


Title: 49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]

Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""

import collections
# input: list of strings
# output: list of list of grouped anagrams

# method 1
class Solution:
    def groupAnagrams(self, strs):
        # map char count of each string to list of anagrams
        res = collections.defaultdict(list)
        for s in strs:
            # count chars, [0, 0, 0, ..., 0]
            c = [0] * 26
            for char in s:
                # add 1 to corresponding c[index] for each occuring letter
                c[ord(char) - ord('a')] += 1
            res[tuple(c)].append(s)
        return res.values()
# method 2         
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        res = []
        pos = 0
        for s in strs:
            sorted_s = ''.join(sorted(s))
            
            if sorted_s not in seen:
                seen[sorted_s] = pos
                res.append([s])
                pos += 1
            else:
                res[seen[sorted_s]].append(s)
        return res
                
