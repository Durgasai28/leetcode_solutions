class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i+1,n+1):
                seen=set(nums[i:j])
                val=len(seen)
                ans+=val*val

        return ans