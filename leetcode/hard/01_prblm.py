"""
-> Largest Color Value in a Directed Graph

There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith 
node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that 
there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed 
edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored 
the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
"""

from collections import defaultdict

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        # Return max freq of color 
        def dfs(node):
            if node in path:
                return float("inf")

            if node in visit:
                return 0
            visit.add(node)
            path.add(node)

            colorIndex = ord(colors[node]) - ord('a')
            count[node][colorIndex] = 1

            for neighbor in adj[node]:
                if dfs(neighbor) == float("inf"):
                    return float("inf")

                for c in range(26):
                    count[node][c] = max(
                        count[node][c],
                        (1 if c == colorIndex else 0) + count[neighbor][c]
                    )
            path.remove(node)
            return max(count[node])

        n, res = len(colors), 0
        visit, path = set(), set()
        count = [[0]* 26 for i in range(n)] # Map count[node][color] -> map freq color
        for i in range(n):
            res = max(dfs(i), res)

        return -1 if res == float("inf") else res


obj = Solution()
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]
print(obj.largestPathValue(colors, edges))