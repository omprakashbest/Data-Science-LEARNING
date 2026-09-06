"""
-> Count Prefix and Suffix Pairs Ⅰ

You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

• isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix,
but isPrefixAndSuffix("abc", "abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], 
words[j]) is true.
"""

class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        res = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w1, w2 = words[i], words[j]
                if w2.startswith(w1) and w2.endswith(w1):
                    res += 1
        return res

obj = Solution()
words = ["aba", "ababa", "abc", "abcd", "a", "aa"]
print(obj.countPrefixSuffixPairs(words))  