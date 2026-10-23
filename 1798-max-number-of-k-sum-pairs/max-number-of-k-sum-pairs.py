class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq={}
        ans=0
        for i in range(len(nums)):
            if freq.get((k-nums[i]),0)>0:
                freq[k-nums[i]]-=1
                ans+=1
            else:
                freq[nums[i]]=freq.get(nums[i],0)+1

        return ans