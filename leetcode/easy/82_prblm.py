"""
-> Lemonade Change 

At a Lemonade stand, each lemonade cost $5. Customers are standing in a queue to buy from you and order one at 
a time (in the order specified by bills.) Each customer will only buy one lemonade and pay with either a $5, $10
and $20 bill. You must provide the correct change to each customer os that the net transaction is that the 
customer pays $5.

Note : that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide 
every customer with the correct change or false otherwise.
"""

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five, ten = 0, 0
        for b in bills:
            if b == 5:
                five += 1
            if b == 10:
                ten += 1

            change = b - 5
            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False
            elif change == 15:
                if five > 0 and ten > 0:
                    five, ten = five - 1, ten - 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

obj = Solution()
bills = [5, 5, 5, 10, 20]
print(obj.lemonadeChange(bills))
