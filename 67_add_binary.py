class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # given 2 binary strings
        # return their sum as a binary string

        # python int(int, base) to convert binary str to integer
        # python format(int, 'b') for conversion from integer to binary without 0b

        return format((int(a,2) + int(b,2)), 'b')
