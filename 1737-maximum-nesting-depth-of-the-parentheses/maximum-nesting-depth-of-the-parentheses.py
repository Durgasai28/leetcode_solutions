class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth=0
        depth=0
        for char in s:
            if char=='(':
                depth+=1
            elif char==')':
                maxdepth=max(depth,maxdepth)
                depth-=1
        return maxdepth