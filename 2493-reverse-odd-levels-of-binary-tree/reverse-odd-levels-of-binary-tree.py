from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        level=0
        que=deque([root])

        while que:
            size=len(que)
            nodes=[]
            for _ in range(len(que)):
                node=que.popleft()
                nodes.append(node)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if level%2 == 1:
                values=[node.val for node in nodes]

                for i in range(size):
                    nodes[i].val=values[size - 1 - i]
            level+=1

        return root