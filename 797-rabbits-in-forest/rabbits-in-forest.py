class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq={}
        for val in answers:
            freq[val]=freq.get(val,0)+1

        ans=0
        for key , val in freq.items():
            size=key+1
            groups = (val+size-1)//size
            ans+=groups*size

        return ans