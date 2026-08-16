"""
-> Kth Distinct String in an Array

A distinct string is string that is present only once in an array.

Given an array of string arr, and an integer k, return the kth distinct string present in arr. if there are 
fewer than k distinct strings, return an empty string "".

Note: that the string are considered in the order in which they appear in the array.
"""


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count = {}

        for s in arr:
            if s not in count :
                count[s] = 0
            count[s] += 1

        for s in arr:
            if count[s] == 1:
                k -= 1
            if k == 0:
                return s
        return ""        

obj = Solution()
arr, k =  ["d","b","c","b","c","a"], 2
print(obj.kthDistinct(arr, k))