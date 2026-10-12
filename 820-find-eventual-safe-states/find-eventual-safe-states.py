class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n=len(graph)
        state=[0]*n

        def dfs(node):
            if state[node]==1:
                return False
            elif state[node]==2:
                return True
            
            state[node]=1

            for val in graph[node]:
                if not dfs(val):
                    return False

            state[node]=2
            return True

        #main
        ans=[]
        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans
        