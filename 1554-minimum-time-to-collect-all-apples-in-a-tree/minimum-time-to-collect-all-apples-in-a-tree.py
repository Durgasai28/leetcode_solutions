class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        graph={i:[] for i in range(n)}
        for sta,end in edges:
            graph[sta].append(end)
            graph[end].append(sta)

        def dfs(node,parent):
            time=0

            for neigh in graph[node]:
                if neigh == parent:
                    continue

                child_time=dfs(neigh,node)
                if child_time>0 or hasApple[neigh]:
                    time+=child_time+2

            return time

        return dfs(0,-1)