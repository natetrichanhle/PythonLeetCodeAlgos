class Solution:
    def climbStairs(self, n: int) -> int:
        # recursive solution

        # # doesn't pass test cases since the time limit is exceeded
        # # base cases
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2 
        # # recursive call
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # (bottom up) dynamic programming solution

        one, two = 1, 1
        # it's n-1 because we have to compute n-1 values after one and two
        for i in range(n - 1):
            # basically fibonacci sequence 
            # we need a temp to store one's value before we set two to one
            temp = one
            one = one + two
            two = temp
        # we return one because it will eventually land on the number of distinct ways we can climb to the top
        return one