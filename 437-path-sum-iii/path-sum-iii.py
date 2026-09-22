# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        ans=0
        def findSum(node,total):
            nonlocal ans
            if not node:
                return

            total+=node.val
            if total==targetSum:
                ans+=1

            findSum(node.left,total)
            findSum(node.right,total)

        def dfs(node):
            if not node:
                return 
            
            findSum(node,0)

            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ans