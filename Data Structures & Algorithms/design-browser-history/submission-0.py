class Node:

    def __init__(self, url: str, prev=None, next=None):
        self.url = url 
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.curr = self.homepage

    def visit(self, url: str) -> None:
        newPage = Node(url)
        self.curr.next, newPage.prev = newPage, self.curr
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr and self.curr.prev:
            if steps == 0:
                return self.curr.url
            self.curr = self.curr.prev
            steps-=1
        return self.curr.url
                
    def forward(self, steps: int) -> str:
        while self.curr and self.curr.next:
            if steps == 0:
                return self.curr.url
            self.curr = self.curr.next
            steps-=1
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)