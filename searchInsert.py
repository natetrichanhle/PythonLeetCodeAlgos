def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            midpoint = (start + end) // 2
            midpoint_value = nums[midpoint]
            if midpoint_value == target:
                return midpoint
            elif target > midpoint_value:
                start = midpoint + 1
            elif target < midpoint_value:
                end = midpoint - 1
        return start 