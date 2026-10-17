class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = {}
        left = 0
        max_fruits=0

        for right in range(len(fruits)):
            val=fruits[right]
            freq[val]=freq.get(val,0)+1
            while len(freq)>2:
                freq[fruits[left]]-=1

                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]

                left+=1

            max_fruits=max(max_fruits,right-left+1)
        return max_fruits
            