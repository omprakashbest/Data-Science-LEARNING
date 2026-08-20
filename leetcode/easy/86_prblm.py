"""
-> Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings words. A string is 
consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str])-> int:
        allowed = set(allowed)

        res = len(words)
        for w in words:
            for ch in w:
                if ch not in allowed:
                    res -= 1
                    break
        return res

obj = Solution()
allowed, words = "ab", ["ad","bd","aaab","baa","badab"]
print(obj.countConsistentStrings(allowed, words))
