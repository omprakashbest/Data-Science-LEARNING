"""
-> Largest Local Values in a Matrix

You are given an n x n integer matrix grid.

Generate an integer matrix maxlocal of size(n - 2) x (n - 2) such that:

• maxlocal[i][j] is equal to the largest value of the 3x3 matrix in grid centered around row i+1 and columns 
j + 1.

In other words, we want to find the largest value in every contiguous 3x3 matrix grid.

Return the generated matrix.
"""

class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        N = len(grid)
        res = [[0] * (N-2) for _ in range(N-2)]

        for i in range(N - 2):
            for j in range(N - 2):
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        res[i][j] = max(res[i][j], grid[r][c])

        return res

obj = Solution()
grid = [[9,9,8,1],
        [5,6,2,6],
        [8,2,6,4],
        [6,2,2,2]]

print(obj.largestLocal(grid))