from collections import deque
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        left=0
        pre_sum=0
        ans=0
        dq=deque()

        for right in range(len(chargeTimes)):
            pre_sum+=runningCosts[right]

            while dq and chargeTimes[dq[-1]]<chargeTimes[right]:
                dq.pop()

            dq.append(right)

            while dq and chargeTimes[dq[0]]+((right-left+1)*pre_sum)>budget:
                pre_sum -= runningCosts[left]

                if dq[0] == left:
                    dq.popleft()
                
                left+=1
            
            ans=max(ans,right-left+1)

        return ans
        