"""
-> Circular Sentence

A sentence is a list of words that are separated by a single space with no leading or trailing spaces 

• for example, "Hello World", "HELLO", "hello world hello world" are all sentences.

Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are 
considered different.

A sentence is circular if:

• The last character of each word in the sentence is equal to the first character of its next word.
• The last character of the last word is equal to the first character of the first word.

For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences.
However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.
"""

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        w = sentence.split(" ") # list of words

        for i in range(len(w)):
            if w[i][0] != w[i-1][-1]:
                return False
        return True

obj = Solution()
sentence = "leetcode exercises sound delightful"
print(obj.isCircularSentence(sentence))