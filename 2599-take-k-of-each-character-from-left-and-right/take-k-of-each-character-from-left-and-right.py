class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq={'a':s.count('a')-k,'b':s.count('b')-k,'c':s.count('c')-k}

        if min(freq.values()) < 0:
            return -1

        n=len(s)
        left=0
        ans=0

        for right in range(len(s)):
            freq[s[right]]-=1

            while freq[s[right]] < 0:
                freq[s[left]]+=1
                left += 1

            ans=max(ans, right-left+1)
                
        return n-ans

