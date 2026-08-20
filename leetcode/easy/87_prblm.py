"""
-> Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other 
sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any 
order.
"""

from collections import defaultdict


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        count = defaultdict(int)

        for w in s1.split(" ") + s2.split(" "):
            count[w] += 1

        res = []
        for w, cnt in count.items():
            if cnt == 1:
                res.append(w)
        return res

obj = Solution()
s1, s2 = "this apple is sweet", "this apple is sour"
print(obj.uncommonFromSentences(s1, s2))
