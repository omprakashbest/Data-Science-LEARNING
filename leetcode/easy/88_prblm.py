"""
-> Minimum String Length after removing Substrings

You are given a string a consisting only of uppercase English letters.

You can are apply some operations to this string where, in one operation, you can remove any  occurrence of one 
of ht substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.

Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.
"""

class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            stack.append(c)

            if (len(stack) >= 2 and (
                (stack[-2] == "A" and stack[-1] == "B") or 
                (stack[-2] == "C" and stack[-1] == "D")
            )):
                stack.pop()
                stack.pop()

        return len(stack)

obj = Solution()
s = "ABFCACDB"
print(obj.minLength(s))