class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)

        if self.tail == self.head:
            self.head.next = newNode
            self.tail = newNode
        else:
            newNode.next = self.head.next
            self.head.next = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        i = 0
        prev, curr = self.head, self.head.next

        while curr:
            if i == index:
                if curr == self.tail:
                    self.tail = prev
                    self.tail.next = None
                else:
                    prev.next = prev.next.next
                return True
            i+=1
            prev = curr
            curr = curr.next
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next

        while curr:
            values.append(curr.val)
            curr = curr.next
        return values
