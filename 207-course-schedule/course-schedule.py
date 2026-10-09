class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        
        def dfs(num,visited):
            if visited[num]==1:
                return False
            if visited[num]==2:
                return True

            visited[num]=1

            for neigh in graph[num]:
                if not dfs(neigh,visited):
                    return False

            visited[num]=2    
            return True

            

        for sta,end in prerequisites:
            graph[end].append(sta)

        visited = [0]*numCourses

        for i in range(numCourses):
            if not dfs(i,visited):
                return False

        return True
        