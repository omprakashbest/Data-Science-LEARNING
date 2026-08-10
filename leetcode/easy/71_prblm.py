"""
-> Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
"""

from collections import defaultdict

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        arr2_set = set(arr2)
        # Create a dictionary to count occurrences of each number in arr1
        arr1_count = defaultdict(int)
        end = []

        for n in arr1:
            if n not in arr2_set:
                end.append(n)    
            arr1_count[n] += 1
        end.sort()

        res = []
        for n in arr2:
            for _ in range(arr1_count[n]):
                res.append(n)
        res.extend(end)
        return res

# Example usage:
obj = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(obj.relativeSortArray(arr1, arr2))