class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        dir_graph={i:[] for i in range(n)}

        for sta,end in edges:
            dir_graph[end].append(sta)

        ans=[]
        for key,nodes in dir_graph.items():
            if not nodes:
                ans.append(key)

        return ans