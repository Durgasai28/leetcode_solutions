# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        freq={}

        def dfs(node,row,col):
            if not node:
                return None

            freq[col] = freq.get(col, [])
            freq[col].append([row, node.val])

            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)

        dfs(root,0,0)

        ans=[]
        for col in sorted(freq):
            freq[col].sort()
            ans.append([val for row,val in freq[col]])

        return ans