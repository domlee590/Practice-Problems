# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        from collections import deque

        if not root:
            return 0
        
        minDepth = 0
        q = deque([root])

        while len(q) > 0:
            minDepth += 1
            levelLen = len(q)

            for i in range(levelLen):
                node = q.popleft()

                if not node.left and not node.right:
                    return minDepth

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)