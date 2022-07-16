# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        
        if not root:
            return []
        
        result = []
        q = deque([root])

        while len(q) > 0:
            total = 0
            levelLen = len(q)
            for i in range(levelLen):
                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(total / levelLen)

        return result
