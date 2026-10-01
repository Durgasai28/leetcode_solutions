# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def dfs(node):
            if not node:
                return 0

            left=dfs(node.left)
            right=dfs(node.right)

            if left==right and left!=-1:
                s=left+right+1
                ans.append(s)
                return s

            return -1

        dfs(root)

        if len(ans)<k:
            return -1

        ans.sort(reverse=True)
        return ans[k-1]