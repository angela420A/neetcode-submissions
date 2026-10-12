class Node:

    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.length = 0

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next

        while curr and curr != self.tail:
            if i == index:
                return curr.val
            curr = curr.next
            i+=1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        nextNode = self.head.next

        self.head.next = nextNode.prev = newNode
        newNode.prev, newNode.next = self.head, nextNode

        self.length += 1
        return

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        prevNode = self.tail.prev

        self.tail.prev = prevNode.next = newNode
        newNode.prev, newNode.next = prevNode, self.tail

        self.length += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            return self.addAtTail(val)
        
        i = 0
        curr = self.head
        while curr and curr != self.tail:
            if i == index:
                newNode = Node(val)
                nextNode = curr.next

                curr.next = nextNode.prev = newNode
                newNode.prev, newNode.next = curr, nextNode

                self.length += 1
                break
            curr = curr.next
            i+=1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        i = 0
        curr = self.head
        while curr and curr != self.tail:
            if i == index:
                nextNode = curr.next.next

                curr.next, nextNode.prev = nextNode, curr

                self.length -= 1
                break
            curr = curr.next
            i += 1
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)