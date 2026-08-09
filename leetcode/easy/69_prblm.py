"""
-> Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words
(including duplicates). You may return the answer in any order.
"""

from typing import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # Count characters of the first word
        cnt = Counter(words[0])

        # Compare character counts with each word
        for w in words:
            cur_cnt = Counter(w)
            # Keep the minimum frequency of each character across all words
            for c in cnt:
                cnt[c] = min(cnt[c], cur_cnt[c])

        res = []
        # Build the result using the common frequencies
        for c in cnt:
            # Add the character as many times as
            # it appears in every word
            for i in range(cnt[c]):
                res.append(c)
        return res

obj = Solution()
words = ["bella","label","roller"]
print(obj.commonChars(words))