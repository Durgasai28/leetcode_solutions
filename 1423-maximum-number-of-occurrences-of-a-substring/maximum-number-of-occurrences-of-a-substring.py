class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ans={}
        freq={}
        left=0

        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1

            while len(freq)>maxLetters or right-left+1>minSize:
                freq[s[left]]-=1

                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1

            if right-left+1==minSize:
                st=s[left:right+1]
                ans[st]=ans.get(st,0)+1
            
        return max(ans.values(), default=0)