class Solution:
    def minInsertions(self, s: str) -> int:
        right=0
        sta=[]
        i=0
        while i<len(s):
            ch=s[i]
            if ch=='(':
                sta.append(ch)
            else:
                if i+1<len(s) and s[i]==s[i+1]:
                    if sta:
                        sta.pop()
                    else:
                        right+=1
                    i+=1
                else:
                    if sta:
                        sta.pop()
                        right+=1
                    else:
                        right+=2
            i+=1

        return len(sta)*2 + right