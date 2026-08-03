"""
Binary Tree Zigzag Level Order Traversal

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values
(i.e., from left to right, then right to left for the next level and alternate between).

Example tree:
          3
        /   \
       9     20
            /  \
           15   7

This module defines a TreeNode and provides zigzagLevelOrder(root) which returns a list of
lists with the zigzag traversal.
"""

from collections import deque
from typing import List, Optional

class TreeNode:
    # Constructor
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root] if root else [])

        while q: # while q not empty
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)

            level = level[::-1] if len(res) % 2 else level
            res.append(level)
        return res

obj = Solution()
# Build the example tree and print the zigzag traversal
#       3
#     /   \
#    9     20
#         /  \
#        15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(obj.zigzagLevelOrder(root))
