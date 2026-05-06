# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def bracktrack(node, valSum):
            if not node:
                return False
            
            valSum += node.val
            if not node.left and not node.right:
                return valSum == targetSum
            
            return bracktrack(node.left, valSum) or bracktrack(node.right, valSum)

        return bracktrack(root, 0)