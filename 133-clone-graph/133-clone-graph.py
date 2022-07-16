"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #https://www.youtube.com/watch?v=mQeF6bN8hMk
        
        if not node:
            return None
        
        oldNewMap = {}
        #create map for deep copy
        
        def clone(node):
            if node in oldNewMap: #return copy node for neightbor assignment
                return oldNewMap[node]
            
            copy = Node(node.val)
            oldNewMap[node] = copy #make copy with value
            
            for nb in node.neighbors: #for each neighbor, append its copy (go into recursive stack until hit node in map)
                copy.neighbors.append(clone(nb))
            return copy #return the copy with neighbors
        
        clone(node)
        
        return oldNewMap[node]