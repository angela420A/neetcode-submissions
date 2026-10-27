class TreeNode:

    def __init__(self, key: int, val: int, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return
        
        curr = self.root
        while True:
            if curr.key > key:
                if not curr.left:
                    curr.left = TreeNode(key, val)
                    break
                curr = curr.left
            elif curr.key < key:
                if not curr.right:
                    curr.right = TreeNode(key, val)
                    break
                curr = curr.right
            else:
                curr.val = val
                break

    def get(self, key: int) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr:
            if curr.key > key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def _findMin(self, root):
        while root.left:
            root = root.left
        return root

    def getMin(self) -> int:
        return self._findMin(self.root).val if self.root else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def _delete(self, root, key):
        if not root:
            return None
        
        if root.key > key:
            root.left = self._delete(root.left, key)
        elif root.key < key:
            root.right = self._delete(root.right, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                minNode = self._findMin(root.right)
                root.key = minNode.key
                root.val = minNode.val
                root.right = self._delete(root.right, minNode.key)
        return root

    def remove(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def _inorder(self, root, res):
        if not root:
            return 
        self._inorder(root.left, res)
        res.append(root.key)
        self._inorder(root.right, res)

    def getInorderKeys(self) -> List[int]:
        res = []
        self._inorder(self.root, res)
        return res