class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=float('inf')

        for i in range(l,r+1):
            total=sum(nums[:i])

            if total>0:
                ans=min(ans,total)
            
            for k in range(i,len(nums)):
                total+=nums[k]-nums[k-i]
                if total>0:
                    ans=min(total,ans)
        return ans if ans!=float('inf') else -1