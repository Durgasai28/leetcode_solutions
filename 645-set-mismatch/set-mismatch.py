class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = set()
        dup=0
        for val in nums:
            if val in seen:
                dup = val
            seen.add(val)

        missing = sum(range(1,len(nums)+1))-sum(nums) + dup

        return [dup, missing]
