"""
Given two strings named needle and haystack.
Return the index of first occurence of needle in haystack.
Return -1 if needle not in haystack.
Return 0 if needle is empty.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # using python String.find() which returns index of first occurence, or -1 if not in string.
        if len(needle) == 0: return 0
        return haystack.find(needle)

        # usign python String.index() which returns index of substring start or error
        # meaning check in haystack first
        if needle not in haystack: return -1
        return haystack.index(needle)



