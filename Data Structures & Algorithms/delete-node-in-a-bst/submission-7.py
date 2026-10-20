# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.delete(root, key)

    def findMin(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if not root:
            return None

        if root.val > key:
            root.left = self.delete(root.left, key)
        elif root.val < key:
            root.right = self.delete(root.right, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minNode = self.findMin(root.right)
                root.val = minNode.val
                root.right = self.delete(root.right, minNode.val)
        return root
