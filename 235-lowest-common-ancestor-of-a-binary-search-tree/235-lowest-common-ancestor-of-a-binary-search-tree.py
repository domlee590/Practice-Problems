# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Use properties of BST. Left smaller, right bigger
        # The LCA happens to be where p and q are on opposite sides of the subtree
        
        pVal = p.val
        qVal = q.val
        
        # Navigate BST based on values
        if pVal > root.val and qVal > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif pVal < root.val and qVal < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root