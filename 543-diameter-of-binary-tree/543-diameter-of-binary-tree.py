# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Use list for "global" access
        maxDiam = [0]
        
        # Will calculate the height of a node based on subtrees (bottom-up)
        def dfs(root):
            # Base case is null subtree, which has height -1
            if not root:
                return -1
            
            # Get subtree heights
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            
            # Current height is the larger subtree's + edge connecting current node to it
            curHeight = 1 + max(leftHeight, rightHeight)
            
            # Largest possible diameter through current node
            curDiam = leftHeight + rightHeight + 2  # Add 2 for edges connecting subtrees
            
            # Update maximum
            maxDiam[0] = max(maxDiam[0], curDiam)
            
            return curHeight
        
        dfs(root)
        return maxDiam[0]