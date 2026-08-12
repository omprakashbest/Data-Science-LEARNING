"""
-> Lucky Numbers in a Matrix

Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its 
column.

"""

class Solution:
    def luckyNumbers(self, matrix: list[list[list[int]]]) -> list[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []

        row_min = set()
        for r in range(ROWS):
            row_min.add(min(matrix[r]))
        col_max = set()
        for c in range(COLS):
            cur_max = matrix[0][c]
            for r in range(ROWS):
                cur_max = max(cur_max, matrix[r][c])
            col_max.add(cur_max)

        for n in row_min:
            if n in col_max:
                res.append(n)

        return res

obj = Solution()
# Example usage:
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(obj.luckyNumbers(matrix))  