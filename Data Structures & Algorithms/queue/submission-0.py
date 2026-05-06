class LindedNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head, self.tail = LindedNode(-1), LindedNode(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.count = 0

    def isEmpty(self) -> bool:
        if self.count > 0:
            return False
        return True

    def append(self, value: int) -> None:
        newNode = LindedNode(value)
        prevNode = self.tail.prev
        
        newNode.prev, newNode.next = prevNode, self.tail
        self.tail.prev = prevNode.next = newNode

        self.count+=1

    def appendleft(self, value: int) -> None:
        newNode = LindedNode(value)
        nextNode = self.head.next

        newNode.prev, newNode.next = self.head, nextNode
        self.head.next = nextNode.prev = newNode

        self.count+=1

    def pop(self) -> int:
        if self.tail.prev == self.head:
            return -1

        popNode = self.tail.prev
        
        prevNode = self.tail.prev.prev
        prevNode.next, self.tail.prev = self.tail, prevNode
        
        self.count-=1
        return popNode.val

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        
        popNode = self.head.next

        nextNode = self.head.next.next
        nextNode.prev, self.head.next = self.head, nextNode

        self.count-=1
        return popNode.val
