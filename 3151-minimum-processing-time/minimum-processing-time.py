class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()

        ans=float('-inf')
        j=0

        for i in range(len(tasks)):
            if i%4==0:
                ans=max(ans,processorTime[j]+tasks[i])
                j+=1
        return ans