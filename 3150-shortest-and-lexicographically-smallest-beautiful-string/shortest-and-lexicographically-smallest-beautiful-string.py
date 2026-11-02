class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left=0
        ans=""
        cou_ones=0

        for right in range(len(s)):
            if s[right]=='1':
                cou_ones+=1

            while cou_ones>k:
                if s[left]=='1':
                    cou_ones-=1
                left+=1
            
            while cou_ones==k and s[left]=='0':
                left+=1
            
            if cou_ones==k:
                curr=s[left:right+1]

                if len(ans)==0 or len(curr)<len(ans) or (len(ans)==len(curr) and curr<ans):
                    ans=curr

        return ans

            