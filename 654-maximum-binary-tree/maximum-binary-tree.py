import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        root=None
        def buildTree(left,right):
            if left>right:
                return None
            
            idx=left
            for i in range(left,right+1):
                if nums[i] >nums[idx]:
                    idx=i

            node=TreeNode(nums[idx])
            root=node

            root.left=buildTree(left,idx-1)
            root.right=buildTree(idx+1,right)

            return root

        return buildTree(0,len(nums)-1)

        