"""
-> Minimum Number of Moves to Seat Everyone

There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position
of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth 
student.

You may perform the following move any number of times:

• Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to 
x + 1 or x - 1).
Return the minimum number of moves required to move each student to a seat such that no two students are in the 
same seat.

Note that there may be multiple seats or students in the same position at the beginning.
"""

from math import remainder


class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        max_index = max(max(seats), max(students)) + 1
        count_seats = [0] * max_index
        count_students = [0] * max_index

        # Count seats at each position
        for seat in seats:
            count_seats[seat] += 1

        # Count students at each position
        for student in students:
            count_students[student] += 1

        i, j = 0, 0
        res = 0
        remain = len(students)

        while remain:
            if count_seats[i] == 0:
                i += 1
            if count_students[j] == 0:
                j += 1

            if count_seats[i] and count_students[j]:
                res += abs(i - j)

                count_seats[i] -= 1
                count_students[j] -= 1
                remain -= 1
        return res

obj = Solution()
seats = [3, 1, 5]
students = [2, 7, 4]
print(obj.minMovesToSeat(seats, students))
