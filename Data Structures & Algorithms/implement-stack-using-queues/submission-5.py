class Node:

    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

class MyStack:

    def __init__(self):
        self.left = self.right = None

    def push(self, x: int) -> None:
        newNode = Node(x)

        if self.left:
            newNode.next = self.left
            self.left = newNode
        else:
            self.left = self.rigth = newNode

    def pop(self) -> int:
        if not self.left:
            return None
        
        val = self.left.val
        self.left = self.left.next
        if not self.left:
            self.right = self.left = None
        return val

    def top(self) -> int:
        if not self.left:
            return None
        return self.left.val

    def empty(self) -> bool:
        if not self.left:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()