# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allPaths = []
        
        def dfs(node, curSum, curPath):
            if not node:
                return
            
            curSum += node.val
            curPath.append(node.val)
            
            if (not node.left and not node.right and
                curSum == targetSum):
                allPaths.append(list(curPath)) #pass by value
            else:
                dfs(node.left, curSum, curPath) #could pass by value but wastes space
                dfs(node.right, curSum, curPath)
            
            #remove last node before moving up call stack
            del curPath[-1]
        
        dfs(root, 0, [])
        return allPaths