class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:        
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)

        newNode.next = self.head.next
        self.head.next = newNode

        if self.tail == self.head:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        prev, curr = self.head, self.head.next
        i = 0

        while curr:
            if i == index:
                if curr == self.tail:
                    self.tail = prev
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
            i += 1
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next

        while curr:
            values.append(curr.val)
            curr = curr.next
        return values