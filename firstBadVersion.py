# def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # [1,2,3,4,5]
#         start = 1
#         end = n
#         while start < end:
#             mid = (start + end) // 2
#             if isBadVersion(mid):
#                 end = mid
#             else:
#                 start = mid + 1
#         return start

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search
        low, high = 1, n
        while low < high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                # this has to be + 1 because we want to find the first bad version not the last good version
                low = mid + 1
        return low
            