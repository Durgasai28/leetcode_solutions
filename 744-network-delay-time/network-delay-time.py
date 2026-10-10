import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph={i:[] for i in range(1,n+1)}

        for sta,end,w in times:
            graph[sta].append((end,w))

        dist=[float('inf')] * (n + 1)
        dist[k]=0

        heap=([(0,k)])
        #heapq.heapify(heap)

        while heap:
            time,node=heapq.heappop(heap)

            if time>dist[node]:
                continue

            for  neigh,weight in graph[node]:
                new_time=time+weight
                if new_time < dist[neigh]:
                    dist[neigh]=new_time
                    heapq.heappush(heap, (new_time, neigh))

        ans=max(dist[1:])

        return ans if ans!=float('inf') else -1