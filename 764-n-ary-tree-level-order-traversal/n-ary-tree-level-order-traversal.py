"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        res=[]
        que=deque([root])

        while que:
            level=[]
            size=len(que)

            for i in range(size):
                node=que.popleft()
                level.append(node.val)

                for child in node.children:
                    que.append(child)
            res.append(level)

        return res