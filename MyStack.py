class MyStack(object):
    # Using a stack

    # def __init__(self):
    #     self.stack = []

    # def push(self, x):
    #     """
    #     :type x: int
    #     :rtype: None
    #     """
    #     self.stack.append(x)

    # def pop(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.stack.pop()

    # def top(self):
    #     """
    #     :rtype: int
    #     """
    #     return self.stack[-1]

    # def empty(self):
    #     """
    #     :rtype: bool
    #     """
    #     if self.stack:
    #         return False
    #     else:
    #         return True

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # return self.queue.pop()
        # OR
        # for every value other than the last one(the one we need to return since queues can only pop from the front)
        for i in range(len(self.queue) - 1):
            # push all the values that were removed from the front of the queue
            self.push(self.queue.popleft())
        # we are returning the left most value of the queue after the loop because it was the last value before the loop iterated.
        return self.queue.popleft()
    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()