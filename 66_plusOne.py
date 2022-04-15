"""
LeetCode Problem: 66. Plus One
TestCases: 111 / 111 test cases passed.
Runtime: 31 ms, faster than 93.50% of Python3 online submissions for Plus One.
Memory Usage: 13.9 MB, less than 63.34% of Python3 online submissions for Plus One.

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Constraints:
    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain any leading 0's.
"""
def plusOne(digits):
    a = list(map(str, digits))
    return [x for x in str(int(''.join(a)) + 1)]


print(plusOne([1,2,3]))
    