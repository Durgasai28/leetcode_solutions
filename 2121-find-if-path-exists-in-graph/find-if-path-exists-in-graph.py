from collections import deque
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph={i:[] for i in range(n)}

        for sta,end in edges:
            graph[sta].append(end)
            graph[end].append(sta)

        que=deque([source])
        visited={source}

        while que:
            node=que.popleft()
            if node==destination:
                return True

            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    que.append(neigh)
        return False


        