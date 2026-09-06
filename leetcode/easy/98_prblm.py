"""
-> Count Prefix and Suffix Pairs II

You are given a 0-indexed string array words.

Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, 
but isPrefixAndSuffix("abc", "abcd") is false.

Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], 
words[j]) is true.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str):
        curr = self.root

        for ch1, ch2 in zip(word, reversed(word)):
            if (ch1, ch2) not in curr.children:
                curr.children[(ch1, ch2)] = TrieNode()
            curr = curr.children[(ch1, ch2)]
            curr.count += 1

    def count(self, word: str):
        curr = self.root

        for ch1, ch2 in zip(word, reversed(word)):
            if (ch1, ch2) not in curr.children:
                return 0
            curr = curr.children[(ch1, ch2)]
        return curr.count

class Solution:

    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        trie = Trie()
        res = 0

        for word in words:
            res += trie.count(word)
            trie.add(word)

        return res