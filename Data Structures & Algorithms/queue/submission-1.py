class LinkedNode:

    def __init__(self, val, pre=None, next=None):
        self.val = val
        self.pre, self.next = pre, next

class Deque:
    
    def __init__(self):
        self.head, self.tail = LinkedNode(-1), LinkedNode(-1)
        self.head.next, self.tail.pre = self.tail, self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        node = LinkedNode(value)
        pre = self.tail.pre

        node.pre, node.next = pre, self.tail
        pre.next = self.tail.pre = node

    def appendleft(self, value: int) -> None:
        node = LinkedNode(value)
        nxt = self.head.next

        node.pre, node.next = self.head, nxt
        nxt.pre = self.head.next = node

    def pop(self) -> int:
        if self.tail.pre == self.head:
            return -1
        rm_node = self.tail.pre
        pre = rm_node.pre
        pre.next, self.tail.pre = self.tail, pre
        return rm_node.val

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        rm_node = self.head.next
        nxt = rm_node.next
        nxt.pre, self.head.next = self.head, nxt
        return rm_node.val
