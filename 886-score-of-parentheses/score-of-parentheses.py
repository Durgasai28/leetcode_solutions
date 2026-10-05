class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        sta=[0]
        for ch in s:
            if ch=='(':
                sta.append(0)
            else:
                val=sta.pop()
                if val == 0:
                    sta[-1]+=1
                else:
                    sta[-1]+=2*val

        return sta[0]