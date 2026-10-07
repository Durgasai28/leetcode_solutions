class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)

        left=[0]*n
        right=[0]*n
        sta=[]

        #left
        for i in range(n):
            while sta and arr[sta[-1]]>arr[i]:
                sta.pop()
            left[i]= i+1 if not sta else i-sta[-1]
            sta.append(i)

        sta=[]
        #right
        for i in range(n-1,-1,-1):
            while sta and arr[sta[-1]]>=arr[i]:
                sta.pop()
            right[i]=n-i if not sta else sta[-1]-i
            sta.append(i)

        ans=0
        for i in range(n):
            ans+=arr[i]*left[i]*right[i]

        return ans%(10**9 + 7)
