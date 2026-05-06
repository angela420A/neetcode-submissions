class TreeNode:

    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)

        if not self.root:
            self.root = newNode
            return
        
        curr = self.root
        while True:
            if curr.key > key:
                if not curr.left:
                    curr.left = newNode
                    return
                curr = curr.left
            elif curr.key < key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if curr.key > key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def _findMin(self, node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMin(self) -> int:
        # curr = self.root
        # while curr and curr.left:
        #     curr = curr.left
        # return curr.val if curr else -1
        res = self._findMin(self.root)
        return res.val if self.root else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self._deleteNode(self.root, key)
    
    def _deleteNode(self, node, key):
        if not node:
            return None
        
        if node.key > key:
            node.left = self._deleteNode(node.left, key)
        elif node.key < key:
            node.right = self._deleteNode(node.right, key)
        else:
            if not node.right:
                return node.left
            elif not node.left:
                return node.right
            else:
                minNode = self._findMin(node.right)
                node.key = minNode.key
                node.val = minNode.val
                node.right = self._deleteNode(node.right, minNode.key)
        return node

    def getInorderKeys(self) -> List[int]:
        result = []
        self._inorderNode(self.root, result)
        return result

    def _inorderNode(self, node, result):
        if not node:
            return
        self._inorderNode(node.left, result)
        result.append(node.key)
        self._inorderNode(node.right, result)

