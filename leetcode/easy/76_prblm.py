"""
-> Sort the People 

You are given an array of strings names, and an array heights that consists of distinct positive integers.
Both arrays are of length n.

for each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.
"""

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        height_to_name = {}
        for h, n in zip(heights, names):
            height_to_name[h] = n

        res = []
        for h in sorted(heights, reverse=True):
            res.append(height_to_name[h])
        return res

obj = Solution()
names = ["Mary", "John", "Emma"]
heights = [180, 165, 170]
print(obj.sortPeople(names, heights))