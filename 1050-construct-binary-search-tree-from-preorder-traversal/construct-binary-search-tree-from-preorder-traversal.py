# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        idx = 0
        n=len(preorder)

        def build(low, high):
            nonlocal idx,n
            if idx==n:
                return None

            if preorder[idx]<low or preorder[idx]>high:
                return None

            root=TreeNode(preorder[idx])
            idx += 1

            root.left=build(low, root.val)
            root.right=build(root.val, high)

            return root

        return build(float('-inf'), float('inf'))