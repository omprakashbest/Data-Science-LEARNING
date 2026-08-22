"""
-> Final Array State After K Multiplication Operations Ⅰ

You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operations:

• final the minimum value x in nums. if there are multiple occurrences of the minimum value, select the one that
appear first.

• Replace an integer array denoting the final state of nums after performing all k operations.
"""

import heapq

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        res = nums[::]

        min_heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(min_heap)

        for _ in range(k):
            val, idx = heapq.heappop(min_heap)

            res[idx] *= multiplier
            heapq.heappush(min_heap, (res[idx], idx))

        return res

obj = Solution()
nums, k, multiplier = [2,1,3,5,6], 5, 2
print(obj.getFinalState(nums, k, multiplier))