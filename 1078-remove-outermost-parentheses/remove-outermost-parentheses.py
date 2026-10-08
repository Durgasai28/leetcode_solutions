class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        sta=[]
        depth=0
        for i in range(len(s)):
            if s[i]=='(':
                if depth > 0:
                    sta.append(s[i])
                depth+=1
            elif s[i]==')':
                depth-=1
                if depth>0:
                    sta.append(s[i])
        return ''.join(sta)


    

        