"""
-> Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result
must be unique and you and return the result in any order ?

"""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set(nums1)

        res = []
        for n in nums2:
            if n in seen:
                res.append(n)
                seen.remove(n)
        return res

obj = Solution()
nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
print(obj.intersection(nums1, nums2))  
