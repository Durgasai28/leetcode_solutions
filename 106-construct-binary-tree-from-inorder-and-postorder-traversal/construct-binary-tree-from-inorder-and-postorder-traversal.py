# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos={}
        for i,val in enumerate(inorder):
            pos[val]=i

        def tree_const(post_l,post_r,in_l,in_r):
            if post_l>post_r:
                return None

            root_val=postorder[post_r]
            root=TreeNode(root_val)

            idx=pos[root_val]
            left_size=idx-in_l

            root.left=tree_const(post_l,post_l+left_size-1,in_l,idx-1)
            root.right=tree_const(post_l+left_size,post_r-1,idx+1,in_r)

            return root

        return tree_const(0,len(postorder)-1,0,len(inorder)-1)