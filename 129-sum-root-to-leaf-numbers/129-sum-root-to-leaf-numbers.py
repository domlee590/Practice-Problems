# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, node, curSum):
        if not node:
            return 0
        
        curSum *= 10 #shift left
        curSum += node.val
        
        if (not node.left and not node.right):
            return curSum
        
        return (self.dfs(node.left, curSum) + self.dfs(node.right, curSum))