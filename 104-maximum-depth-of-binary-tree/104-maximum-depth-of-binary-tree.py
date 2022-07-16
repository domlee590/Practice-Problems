# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        from collections import deque
        
        if not root:
            return 0
        
        numLevels = 0
        q = deque([root])
        
        while len(q) > 0:
            numLevels += 1
            levelSize = len(q)
            
            for _ in range(levelSize):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return numLevels