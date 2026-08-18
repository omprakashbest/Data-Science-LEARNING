"""
-> N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated
by the null value(See examples).
"""

from typing import Optional

class Node:
    def __init__(self, val: Optional[int]=None, children: Optional[list['Node']] = None):
        self.val = val
        self.children =  children if children is not None else []

class Solution:
    def postOrder(self, root: 'Node') -> list[int]:
        res = []
        def helper(node):
            if not node:
                return
            for c in node.children:
                helper(c)
            res.append(node.val)
        helper(root)
        return res

obj = Solution()

# Create nodes
root = Node(1)
node3 = Node(3)
node2 = Node(2)
node4 = Node(4)

node5 = Node(5)
node6 = Node(6)

# Connect children
root.children = [node3, node2, node4]
node3.children = [node5, node6]

print(obj.postOrder(root))