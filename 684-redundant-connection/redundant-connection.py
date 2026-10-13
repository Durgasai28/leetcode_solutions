class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n=len(edges)
        graph = {i:[] for i in range(1,n+1)}

        def dfs(sta,end,seen):
            if sta==end:
                return True

            seen.add(sta)
            for node in graph[sta]:
                if node not in seen:
                    if dfs(node,end,seen):
                        return True

            return False
            
        #main
        ans=[]
        for sta,end in edges:
            seen=set()
            if dfs(sta,end,seen):
                ans=[sta,end]
            else:
                graph[sta].append(end)
                graph[end].append(sta)
        return ans

