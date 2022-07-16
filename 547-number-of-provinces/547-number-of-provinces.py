class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(isConnected, visited, i):
            for j in range(len(isConnected)):
                if(isConnected[i][j] == 1 and visited[j]==0):
                    visited[j] = 1
                    dfs(isConnected, visited, j)
        
        visited = [0 for i in range(len(isConnected))]
        provinces = 0
        
        for i in range(len(isConnected)):
            if visited[i] == 0:
                dfs(isConnected, visited, i)
                provinces += 1
            
        return provinces