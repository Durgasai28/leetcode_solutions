class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)

        ans=0
        left=0
        right = len(nums)-1
        positive = (len(nums)+1)//2

        while left <= right:
            if right >= len(nums)-positive:
                ans+=nums[right]**2
            else:
                ans-=nums[right]**2

            right-=1

        return ans