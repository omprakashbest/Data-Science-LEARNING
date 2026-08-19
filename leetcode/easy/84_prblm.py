"""
-> Convert 1D Array Into 2D Array

You are given a 0-indexed 1-dimensional (1D) integer array original,and two integers, m and n You are tasked with
creating a 2-dimensional(2D) array with m rows and n columns using all the elements from original.

The elements from indices 0 to n - 1(inclusive) of original should form the first row of the constructed
2D array, the elements from indices n to 2*n-1(inclusive) should form the second row of the constructed 2D array
and so on.

Return an mxn 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.
"""

class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int)-> list[list[int]]:
        if len(original) != m*n:
            return []
        res = []

        for r in range(m):
            start = r * n
            end = start + n
            res.append(original[start:end])
        return res

obj = Solution()
original = [1,2,3,4]
m = 2
n = 2
print(obj.construct2DArray(original, m, n))