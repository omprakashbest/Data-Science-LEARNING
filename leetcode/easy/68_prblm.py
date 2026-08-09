"""
-> Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""

from collections import defaultdict

class Solution:
    def LongestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        res = 0

        for ch in s:
            count[ch] += 1
            if count[ch] % 2 == 0:
                res += 2

        for cnt in count.values():
            if cnt % 2:
                res += 1
                break
        return res

obj = Solution()
s = "abccccdd"
print(obj.LongestPalindrome(s)) 