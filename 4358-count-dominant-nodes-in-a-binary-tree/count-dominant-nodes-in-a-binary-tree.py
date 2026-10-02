# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        ans=0
        def postorder(node):
            nonlocal ans
            if not node:
                return float('-inf')
            left=postorder(node.left)
            right=postorder(node.right)
            max_ele=max(left,right,node.val)

            if node.val==max_ele:
                ans+=1
            return max_ele
        postorder(root)
        return ans