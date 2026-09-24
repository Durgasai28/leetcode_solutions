# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
        def inorder(node,l):
            if not node:
                return l
            inorder(node.left,l)
            l.append(node.val)
            inorder(node.right,l)

            return l

        l1=inorder(root1,[])
        l2=inorder(root2,[])
        
        ans=[]
        i,j=0,0

        while i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                ans.append(l1[i])
                i+=1
            else:
                ans.append(l2[j])
                j+=1

        while i<len(l1):
            ans.append(l1[i])
            i+=1
        while j<len(l2):
            ans.append(l2[j])
            j+=1

        return ans
            

        