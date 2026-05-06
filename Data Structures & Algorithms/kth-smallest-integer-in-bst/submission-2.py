# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr, stack = root, []

        while curr or len(stack) > 0:
            # to check node.right is not null
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # if node.right is null, then pop the previous left node
            # otherwise, pop the right side of the node
            curr = stack.pop()
            k-=1
            if k == 0:
                return curr.val
            curr = curr.right