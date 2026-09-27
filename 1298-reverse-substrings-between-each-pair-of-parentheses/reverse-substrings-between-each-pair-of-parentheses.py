class Solution:
    def reverseParentheses(self, s: str) -> str:
        pair=[0]*len(s)
        stack = []
        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(i)
            elif ch==')':
                j=stack.pop()
                pair[i]=j
                pair[j] =i
        i=0
        direction=1
        ans=""
        while 0<=i<len(s):
            if s[i] in '()':
                i=pair[i]
                direction*=-1
            else:
                ans+=s[i]
            i+=direction

        return ans
