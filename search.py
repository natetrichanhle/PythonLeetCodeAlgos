def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # start = 0
        # end = len(nums) - 1
        # while start < end:
        #     midpoint = (start + end) // 2
        #     midpoint_value = nums[midpoint]
        #     if midpoint_value == target:
        #         return midpoint
        #     elif target < midpoint_value:
        #         end = midpoint - 1
        #     elif target > midpoint_value:
        #         start = midpoint + 1
        # return -1

        # More efficient solution
        left, right = 0, len(nums) - 1
        while left <= right:
            midpoint = left + (right - left) // 2
            midpoint_value = nums[midpoint]
            if midpoint_value > target:
                right = midpoint - 1
            elif midpoint_value < target: 
                left = midpoint + 1
            else:
                return midpoint
        return -1

        # Binary Search 

        left, right = 0, len(nums) - 1
        while left <= right:
            midpoint = (left + right) // 2
            midpoint_value = nums[midpoint]
            if target < midpoint_value:
                right = midpoint - 1 
            elif target > midpoint_value:
                left = midpoint + 1
            else:
                return midpoint
        return - 1