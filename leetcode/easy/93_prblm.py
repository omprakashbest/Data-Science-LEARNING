"""
-> Take Gifts From the Richest Pile

You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the 
following:

• Choose the pile with the maximum number of gifts.
• if there is more than one pile with the maximum number of gifts, choose any.
• Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile

Return the number of gifts remaining after k seconds.
"""

import heapq, math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            n = -heapq.heappop(gifts) # -1 * heapq...
            heapq.heappush(gifts, -math.floor(math.sqrt(n)))

        return -sum(gifts)

obj = Solution()
gifts, k = [25, 64, 9, 4, 100], 4
print(obj.pickGifts(gifts, k))