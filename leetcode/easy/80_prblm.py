"""
-> Make Two Arrays Equal by Reversing Subarrays

You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty
subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.
"""

from collections import defaultdict
from typing import Counter

class Solution:
    # first Solution
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)


    # Second Solution
    def canBeEqual2(self, target: list[int], arr: list[int]) -> bool:
        count1, count2 = defaultdict(int), defaultdict(int)

        for n1, n2 in zip(target, arr):
            count1[n1] += 1
            count2[n2] += 1

        if len(count1) != len(count2):
            return False

        for n in count1:
            if count1[n] != count2[n]:
                return False
        return True

obj = Solution()

target = [1,2, 3, 4]
arr = [2, 4, 1, 3]

print(obj.canBeEqual(target, arr))
print(obj.canBeEqual2(target, arr))


