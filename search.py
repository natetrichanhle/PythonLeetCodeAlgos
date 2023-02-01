def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin_index = 0
        end_index = len(nums) - 1

        while begin_index <= end_index:
            self = begin_index + (end_index - begin_index) // 2
            midpoint_value = nums[self]

            if midpoint_value == target:
                return self
            elif target < midpoint_value:
                end_index = self - 1
            elif target > midpoint_value:
                begin_index = self + 1
        return -1