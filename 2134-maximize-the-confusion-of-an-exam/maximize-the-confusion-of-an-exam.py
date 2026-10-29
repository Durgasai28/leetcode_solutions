class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_values=0
        f_values=0
        ans=float('-inf')
        left=0

        for right in range(len(answerKey)):
            if answerKey[right]=='T':
                t_values+=1
            else:
                f_values+=1

            while min(t_values, f_values)>k and left<len(answerKey):
                if answerKey[left]=='T':
                    t_values-=1
                else:
                    f_values-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans