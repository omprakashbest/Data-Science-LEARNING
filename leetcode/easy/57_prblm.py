"""
-> Maximum Odd Binary Number

You given a binary string s that contains at least one '1'.
You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that
can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given condition.
Note: that the resulting string can have leading zeros.
"""
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0 # count number of ones

        for c in s:
            if c == "1":
                count += 1
        return (count - 1) * "1" + (len(s) - count) * "0" + "1"

obj = Solution()
s = "0101"
print(obj.maximumOddBinaryNumber(s))