"""
-> Defuse the Bomb

You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array 
code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

• If k > 0, replace the ith number with the sum of the next k numbers.
• If k < 0, replace the ith number with the sum of the previous -k numbers.
• If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
"""

class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        res = [0] * N

        l = 0
        cur_sum = 0
        for r in range(N + abs(k)):
            cur_sum += code[r % N]

            if r - l + 1 > abs(k):
                cur_sum -= code[l % N]
                l = (l + 1) % N

            if r - l + 1 == abs(k):
                if k > 0:
                    res[(l - 1) % N] = cur_sum
                if k < 0:
                    res[(r + 1) % N] = cur_sum
        return res

obj = Solution()
code, k = [5,7,1,4], 3
print(obj.decrypt(code, k))