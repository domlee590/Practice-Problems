class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool: 
        #Convert edge list to adjacency map
        graph = dict()
        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
            graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]
        
        #Perform search
        return self.dfs(graph, source, destination, set())
    
    def dfs(self, graph, src, trg, visited):
        if src == trg:
            return True
        for nb in graph[src]:
            if nb not in visited:
                visited.add(nb)
                #Only return if True, continue if false
                if self.dfs(graph, nb, trg, visited): return True
        return False