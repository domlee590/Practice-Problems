# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, low = -math.inf, high = math.inf):
            if not root: #empty tree case
                return True
            
            if root.val >= high or root.val <= low:
                return False
            
            if validate(root.left, low, root.val):
                if validate(root.right, root.val, high):
                    return True
            
            return False
        
        return validate(root)
            