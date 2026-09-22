# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        arr = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        def build(l,r):
            if l > r:
                return None

            mid=(l+r)//2
            root=TreeNode(arr[mid])
            root.left =build(l, mid-1)
            root.right=build(mid+1,r)

            return root

        inorder(root)
        return build(0,len(arr)-1)