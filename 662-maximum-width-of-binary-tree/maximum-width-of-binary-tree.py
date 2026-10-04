from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        res=0
        que=deque([(root,0)])

        while que:
            size=len(que)
            left=que[0][1]
            right=que[-1][1]
            res=max(res,right-left+1)

            for _ in range(size):
                node,i = que.popleft()
                
                if node.left:
                    que.append((node.left,2*i))
                if node.right:
                    que.append((node.right,2*i+1))
        return res