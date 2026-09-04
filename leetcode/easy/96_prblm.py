"""
-> String Matching in an Array

Given an array of strings words, return all strings in words that are a substring of another word in any 
order. You can return the answer in any order.

"""

class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                if words[i] in words[j]:
                    res.append(words[i])
                    break 
        return res

obj = Solution()
words = ["mass","as","hero","superhero"]
print(obj.stringMatching(words))