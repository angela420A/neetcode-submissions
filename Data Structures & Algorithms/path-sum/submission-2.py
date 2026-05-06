# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtrack(node, res):
            if not node:
                return False
            res += node.val

            if not node.left and not node.right and res == targetSum:
                return True
            if backtrack(node.left, res):
                return True
            if backtrack(node.right, res):
                return True
            res -= node.val
            return False

        return backtrack(root, 0)