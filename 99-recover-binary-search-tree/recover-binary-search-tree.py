# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.pre=None
        self.first=None
        self.second=None

        def inorder(node):
            if not node:
                return None
            
            inorder(node.left)

            if self.pre and self.pre.val>node.val:
                if self.first is None:
                    self.first=self.pre

                self.second=node

            self.pre=node

            inorder(node.right)


        inorder(root)
        self.first.val,self.second.val=self.second.val,self.first.val