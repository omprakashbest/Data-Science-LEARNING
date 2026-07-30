"""
-> Find the Town Judge 

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town
judge.

if the town judge exist, then:
• The town judge trust nobody.
• Everybody (except for the town judge) trusts the town judge.
• There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trust the person
labeled bi. if a trust relationship does not exist in trust array. then such a trust relationship does not exist.

Return the label of the town judge if the town judge exist and can be identified, or return -1 otherwise.

"""
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1

        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i
        return -1

obj = Solution()
n, trust = 2, [[1, 2]]
print(obj.findJudge(n, trust))