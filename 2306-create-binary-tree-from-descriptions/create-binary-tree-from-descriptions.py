# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        root=None
        hashmap={}
        childs=set()
        
        for par,child,left in descriptions:
            if par not in hashmap:
                hashmap[par] = TreeNode(par)
            if child not in hashmap:
                hashmap[child] = TreeNode(child)

            par_node=hashmap[par]
            child_node=hashmap[child]

            if left==1:
                par_node.left=child_node
            else:
                par_node.right=child_node

            childs.add(child)

        for par,child,left in descriptions:
            if par not in childs:
                root=hashmap[par]
                break

        return root