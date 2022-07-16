# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        q = deque([root])
        backwards = False

        while len(q) > 0:
            level = []
            level_length = len(q)

            for i in range(level_length):
                node = q.popleft()
                if backwards:
                    level.insert(0, node.val)
                else:
                    level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)
            backwards = not backwards

        return result