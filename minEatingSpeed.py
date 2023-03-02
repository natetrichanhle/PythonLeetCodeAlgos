class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        # res is what we're going to be returning hence the minimum integer k
        res = R
        while L <= R:
            # k is the midpoint of the range
            k = L + (R - L) // 2
            # keep track of hours in comparison to H
            hours = 0
            for p in piles:
                # we use math.ceil to round up (p / k is the piles[i] divided by the k value to get the hours(time) that it takes to eat pile)
                hours += math.ceil(p / k)
            # the binary search arguments
            # the right pointer is moved left of k if the hours is less than h 
            if hours <= h:
                # we are trying to find the minimum integer k
                res = min(res, k)
                R = k - 1
            else:
                L = k + 1
        return res