class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def brackets(s,open,close,res,n):
            if len(s)==2*n:
                res.append(s)
                return 
            if open<n:
                brackets(s+'(',open+1,close,res,n)
            if open>close:
                brackets(s+')',open,close+1,res,n)

        res=[]
        brackets("",0,0,res,n)
        return res
