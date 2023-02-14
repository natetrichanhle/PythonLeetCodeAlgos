class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n <= 1:
            return n
        # recursive call
        return self.fib(n-1) + self.fib(n-2)