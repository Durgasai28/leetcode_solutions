class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        check=[True]*len(targets)

        for i in range(len(targets)):
            idx=indices[i]
            if s[idx:idx+len(sources[i])] != sources[i]:
                check[i]=False
        #print(check)
        
        arr = []
        for i in range(len(indices)):
            arr.append((indices[i],sources[i],targets[i],check[i]))

        arr.sort(reverse=True)

        for idx, source,target,valid in arr:
            if valid:
                s = s[:idx]+target+s[idx+len(source):]
        return s