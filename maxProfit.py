class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # l, r = 0, 1
        # max_profit = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         max_profit = max(max_profit, profit)
        #     else:
        #         l = r
        #     r += 1
        # return max_profit

        # two pointer technique (sliding window)
        # iterate through the whole list
        # if the buying point is less than the selling point
        # find the maximum profit 
        # else we want to make the buying point the selling point because that means the buying point is greater than the selling point
        # increase the window at every iteration 
        # return the max profit

        buy, sell = 0, 1
        max_profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1
        return max_profit