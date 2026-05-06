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

    def findMin(self, node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1
        # if self.root:
        #     node = self.findMin(self.root)
        #     return node.val
        # return -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def deleteNode(self, node, key):
        if not node:
            return None
        
        if node.key > key:
            node.left = self.deleteNode(node.left, key)
        elif node.key < key:
            node.right = self.deleteNode(node.right, key)
        else:
            if not node.right:
                return node.left
            elif not node.left:
                return node.right
            else:
                minNode = self.findMin(node.right)
                node.key = minNode.key
                node.val = minNode.val
                node.right = self.deleteNode(node.right, minNode.key)
        return node

    def remove(self, key: int) -> None:
        self.root = self.deleteNode(self.root, key)

    def getInorderKeys(self) -> List[int]:
        res = []
        self.runInorderTreeNode(self.root, res)
        return res

    def runInorderTreeNode(self, node, res) -> None:
        if not node:
            return
        self.runInorderTreeNode(node.left, res)
        res.append(node.key)
        self.runInorderTreeNode(node.right, res)


