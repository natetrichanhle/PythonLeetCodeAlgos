def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # [1,2,3,4,5]
        start = 1
        end = n
        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start