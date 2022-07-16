# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque as queue
        
        if not root:
            return []
        
        res = deque([])
        q = queue([root])
        
        while q:
            levelSize = len(q)
            level = []
            
            for _ in range(levelSize):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.appendleft(level)
        
        return res