"""
Title: 14_longest_common_prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string. 

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # brute force the answer
        # take first word as comparison
        # remove last letter of comparison variable 
        res = strs[0]
        for word in strs:
            while not word.startswith(res):
                res = res[:-1]
        return res

