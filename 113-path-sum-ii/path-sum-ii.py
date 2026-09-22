# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans=[]
        def dfs(node,total,arr):
            if not node:
                return 

            total+=node.val
            arr.append(node.val)

            if not node.left and not node.right and total == targetSum:
                ans.append(arr[:])

            dfs(node.left,total,arr)
            dfs(node.right,total,arr)
            
            arr.pop()

        
        dfs(root,0,[])
        return ans