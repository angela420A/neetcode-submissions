class ListNode:
    
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i+=1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        currNode = ListNode(val)
        currNode.next = self.head.next
        self.head.next = currNode

        if not currNode.next:
            self.tail = currNode

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur:
            i+=1
            cur = cur.next
        
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False
        
    def getValues(self) -> List[int]:
        res = []
        cur = self.head.next
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res
        
