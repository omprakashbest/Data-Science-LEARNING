"""
-> Make The string great

Given a string s of lower an upper case english letters.

A good string is a string which doesn't have two adjacent character s[i] and s[i + 1] where:
• 0 <= i <= s.length - 2
• s[i] is a lower-case and s[i + 1] is the same letter but in upper-case or vice-versa.

To make the string good, you can choose two adjacent character that make the string bad and remove them. you 
can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under tha given constraints.
Notice: that an empty string is also good.
"""

class Solution:
    def makeGood(Self, s: str) -> str:
        stack = []

        i = 0
        while i < len(s):
            if (stack and stack[-1] != s[i] and stack[-1].lower() == s[i].lower()):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)

obj = Solution()
s = "leEeetcode" 
print(obj.makeGood(s))
