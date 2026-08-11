"""
-> Water Bottle

There are numBottles water bottles that are initially full of water. You are exchange numExchange empty water
bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0 # drink
        empty = 0

        while numBottles > 0:
            res += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange

        return res

obj = Solution()
numBottles = 9
numExchange = 3
print(obj.numWaterBottles(numBottles, numExchange))