class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        right=0
        sta=[]

        for ch in s:
            if ch=='(':
                sta.append(ch)
            else:
                if sta:
                    sta.pop()
                else:
                    right+=1

        return len(sta)+right