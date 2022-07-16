class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last = len(graph) -1
        
        paths = []
        
        def backTrack(node, path):
            #base case
            if(node == last):
                paths.append(path.copy()) #DEEP COPY OF VAR
                return
            
            for nextNode in graph[node]:
                path.append(nextNode)
                backTrack(nextNode, path)
                path.pop()
            
        backTrack(0, [0])
        
        return paths
                