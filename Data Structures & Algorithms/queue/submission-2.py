class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = self.right = ListNode(0)

    def isEmpty(self) -> bool:
        if self.left == self.right:
            return True
        return False

    def append(self, value: int) -> None:
        newNode = ListNode(value)
      
        self.right.next, newNode.prev = newNode, self.right
        self.right = newNode

    def appendleft(self, value: int) -> None:
        if self.left == self.right:
            self.append(value)
            return

        newNode = ListNode(value)
        nextNode = self.left.next

        self.left.next, nextNode.prev = newNode, newNode
        newNode.prev, newNode.next = self.left, nextNode

    def pop(self) -> int:
        if self.left == self.right:
            return -1
        
        val = self.right.val
        self.right = self.right.prev
        self.right.next = None
        return val

    def popleft(self) -> int:
        if self.left == self.right:
            return -1

        popNode = self.left.next
        if popNode == self.right:
            self.right = self.left
            self.right.next = None
        else:
            nextNode = popNode.next
            self.left.next, nextNode.prev = nextNode, self.left
        return popNode.val

