class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        graph = dict()
        
        # Create adjacency map from edge list
        for edge in edges:
            graph[edge[0]] = graph.get(edge[0], []) + [edge[1]]
            graph[edge[1]] = graph.get(edge[1], []) + [edge[0]]
        
        # Iterate through nodes
        for node in range(n):
            # Skip nodes of visited components
            if node not in visited:
                self.dfs(graph, node, visited)
                count += 1 # Increment count when unvisited node found (and component visited)
        
        return count
    
    def dfs(self, graph, node, visited):
        # Skip node visited in this component
        if node in visited:
            return
        
        visited.add(node)
        
        # Get [], edge case for singleton nodes
        for neighbor in graph.get(node, []):
            self.dfs(graph, neighbor, visited)
