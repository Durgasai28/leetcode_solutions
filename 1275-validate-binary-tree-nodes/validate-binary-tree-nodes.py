class Solution:
    def validateBinaryTreeNodes(self, n: int, leftchild: list[int], rightchild: list[int]) -> bool:
        visited = set()
        def dfs(node):
            if node == -1:
                return True
            if node in visited:
                return False

            visited.add(node)
            return dfs(leftchild[node]) and dfs(rightchild[node])

        seen=set()
        for i in range(n):
            if leftchild[i]!=-1:
                if leftchild[i] not in seen:
                    seen.add(leftchild[i])
                else:
                    return False
            if rightchild[i]!=-1:
                if rightchild[i] not in seen:
                    seen.add(rightchild[i])
                else:
                    return False

        root = -1 
        for i in range(n): 
            if i not in seen: 
                if root != -1: 
                    return False 
                root = i

        if not dfs(root):
            return False

        return len(visited)==n