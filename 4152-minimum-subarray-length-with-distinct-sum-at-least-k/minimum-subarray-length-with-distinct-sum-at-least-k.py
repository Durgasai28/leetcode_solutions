class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        freq={}
        left=0
        pre_sum=0
        ans=float('inf')

        for right in range(len(nums)):
            if nums[right] not in freq:
                pre_sum+=nums[right]
            
            freq[nums[right]]=freq.get(nums[right],0)+1
            

            while pre_sum>=k:
                ans=min(ans,right-left+1)
                freq[nums[left]]-=1

                if freq[nums[left]]==0:
                    pre_sum-=nums[left]
                    del freq[nums[left]]
                left+=1

        return ans if ans!=float('inf') else -1
                