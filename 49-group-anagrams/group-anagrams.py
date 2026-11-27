class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq={}
        for s in strs:
            key=list(s)
            key.sort()
            key=''.join(key)

            if key in freq:
                freq[key].append(s)
            else:
                freq[key] = [s]

        ans=[]
        for val in freq.values():
            ans.append(val)
        return ans