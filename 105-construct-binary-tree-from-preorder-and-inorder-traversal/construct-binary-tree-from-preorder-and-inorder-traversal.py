# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos={}
        for i,val in enumerate(inorder):
            pos[val]=i

        def Tree_const(pre_l,pre_r,in_l,in_r):
            if pre_l>pre_r:
                return None

            root_val=preorder[pre_l]
            root=TreeNode(root_val)

            idx=pos[root_val]
            left_size=idx-in_l

            root.left=Tree_const(pre_l+1,pre_l+left_size,in_l,idx-1)
            root.right=Tree_const(pre_l+left_size+1,pre_r,idx+1,in_r)

            return root

        return Tree_const(0,len(preorder)-1,0,len(inorder)-1)