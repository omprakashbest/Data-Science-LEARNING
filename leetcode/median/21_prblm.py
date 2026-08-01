"""
-> Capacity To Ship Package within D Days

A conveyor belt has package that must be shipped from one port to anther within days days.

The ith package on the conveyor belt has a weight of weight[i]. Each day, we load the ship with packages on the
conveyor belt(in the order given by weights). We may not load more weight than the maximum weight capacity of
the ship.

Return the least weight capacity of the ship that will result in all the package on the conveyor belt being 
shipped within days days.

"""

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap

            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res

obj = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]; days = 5
print(obj.shipWithinDays(weights, days))