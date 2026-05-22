class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0, 0), Node(0, 0)  # left: least recently used; right: most recently uesd
        self.left.next, self.right.prev = self.right, self.left

        self.capacity = capacity
        self.cache = {}  # key: key, val: Node(key, val)

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)  # Upsert
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.left.next
            self._remove(node)
            del self.cache[node.key]
