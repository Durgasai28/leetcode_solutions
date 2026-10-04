# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: TreeNode | None) -> bool:
        def check(level,stage):
            if stage%2 == 0:
                for i in range(len(level)):
                    if level[i] % 2 == 0:
                        return False
                    if i > 0 and level[i - 1] >= level[i]:
                        return False
            else:
                for i in range (len(level)):
                    if level[i] % 2 != 0:
                        return False

                    if i > 0 and level[i-1] <= level[i]:
                        return False
            return True


        que=deque([root])
        stage=0
        while que:
            level=[]
            size=len(que)

            for i in range(size):
                node=que.popleft()
                level.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if check(level,stage)==False:
                return False
            stage+=1
        return True