# Doubly Linked List
class ListNode:
    def __init__ (self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
    def forward(self, steps: int) -> str:  
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

# Array -> more efficient

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = 0
        self.len = 1
        self.history = [homepage]
    def visit(self, url: str) -> None:
        if len(self.history) < self.curr + 2:
            self.history.append(url)
        else:
            self.history[self.curr + 1] = url
        self.curr += 1
        self.len = self.curr + 1
    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]
    def forward(self, steps: int) -> str:  
        self.curr = min(self.curr + steps, self.len - 1)
        return self.history[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)