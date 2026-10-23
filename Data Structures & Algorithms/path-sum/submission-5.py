# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtrack(root, sumNum):
            if not root:
                return False
            
            sumNum += root.val
            if not root.left and not root.right and sumNum == targetSum:
                return True
            if backtrack(root.left, sumNum):
                return True
            if backtrack(root.right, sumNum):
                return True
            sumNum -= root.val
            return False
        return backtrack(root, 0)
            
            