class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        ans=0
        left=0
        total=0

        for right in range(len(arr)):
            total+=arr[right]

            while (right-left+1)>k:
                total-=arr[left]
                left+=1

            if right-left+1==k and total//(right-left+1)>=threshold:
                ans+=1
        return ans