class Solution:
    def minDeletions(self, s: str) -> int:
        freq={}
        for val in s:
            freq[val]=freq.get(val,0)+1
        
        ans=0
        seen=set()

        for val in sorted(freq.values(),reverse=True):
            while val>0 and val in seen:
                val-=1
                ans+=1

            if val>0:
                seen.add(val)

        return ans