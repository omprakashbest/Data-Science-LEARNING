"""
-> Minimum Bit Flips to Convert Number

A bit flip of a number x is choosing a but in the binary representation of x and flipping it from either 0 to 
1 or 1 to 0

• For example: for x = 7, the binary representation is 111 and we may choose any bit (including any leading 
zeros not shown) and flip it. we can flip the first bit from the right to get 110, flip the
second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc. 

Given two integers start and goal, return the minimum number of but flips to convert start to goal.
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0

        while start or goal:
            if (start & 1) != (goal & 1):
                res += 1
            start = start // 2
            goal = goal // 2

        return res

obj = Solution()
start, goal = 10, 7
print(obj.minBitFlips(start, goal))
