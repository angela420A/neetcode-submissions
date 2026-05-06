class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        leftVal = self.q.pop()
        return leftVal

    def top(self) -> int:
        leftVal = self.q.pop()
        self.push(leftVal)
        return leftVal

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()