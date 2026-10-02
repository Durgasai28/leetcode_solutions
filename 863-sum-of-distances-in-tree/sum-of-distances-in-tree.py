from collections import deque
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph={i:[] for i in range(n)}
        for sta,end in edges:
            graph[sta].append(end)
            graph[end].append(sta)

        count=[1]*n
        res=[0]*n

        def dfs1(node, parent):
            for neig in graph[node]:
                if neig==parent:
                    continue
                dfs1(neig,node)
                count[node] += count[neig]
                res[node] += res[neig]+count[neig]

        def dfs2(node, parent):
            for neig in graph[node]:
                if neig==parent:
                    continue
                res[neig] = (res[node]-count[neig]+(n - count[neig]))
                dfs2(neig,node)

        dfs1(0,-1)
        dfs2(0,-1)

        return res