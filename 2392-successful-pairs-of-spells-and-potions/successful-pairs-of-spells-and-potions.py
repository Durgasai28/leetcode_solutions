class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        ans=[]
        n=len(potions)
        potions.sort()

        for val in spells:
            left=0
            right=n-1
            index=n

            while left<=right:
                mid=(left + right)//2

                if val*potions[mid]>=success:
                    index=mid
                    right=mid-1
                else:
                    left=mid+1

            ans.append(n-index)

        return ans      