class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyStack:

    def __init__(self):
        self.left = self.right = ListNode(0)

    def push(self, x: int) -> None:
        newNode = ListNode(x)
        
        self.right.next, newNode.prev = newNode, self.right
        self.right = newNode

    def pop(self) -> int:
        val = self.right.val
        self.right = self.right.prev
        self.right.next = None
        return val

    def top(self) -> int:
        return self.right.val

    def empty(self) -> bool:
        if self.left == self.right:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()