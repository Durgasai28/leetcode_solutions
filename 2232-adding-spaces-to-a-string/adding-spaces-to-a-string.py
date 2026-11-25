class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        ans=""
        i=0
        right=0

        while right<len(s):
            if i < len(spaces) and right==spaces[i]:
                ans+=" "
                i+=1
            ans+=s[right]
            right+=1
        return ans
