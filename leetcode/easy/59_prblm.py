"""
-> Maximum Nesting Depth of the Parentheses

Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number
of nested parentheses.

"""

class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cur = 0
        
        for c in s:
            if c == '(':
                cur += 1
            elif c == ')':
                cur -= 1
            res = max(res, cur)
        return res

obj = Solution()
s = "(1+(2*3)+((8)/4))+1"
print(obj.maxDepth(s))