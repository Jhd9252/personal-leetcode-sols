# -*- coding: utf-8 -*-
"""


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
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        HashMap {sortedKey : [anagrams]}
        - sort each word
        - check each word against hashmap
        """
        hashmap = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in hashmap:
                hashmap[sorted_word] = []
            hashmap[sorted_word].append(word)
        return list(hashmap.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for word in strs:
            hashmap[tuple(sorted(word))].append(word)
        return list(hashmap.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for word in strs:
            tmp = [0] * 26 # fixed size, 26 letter alphabet
            for char in word:
                tmp[ord(char) - ord('a')] += 1
            hashmap[tuple(tmp)].append(word)
        return list(hashmap.values())