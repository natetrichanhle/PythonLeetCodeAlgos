def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return sorted([num ** 2 for num in nums]) --> more efficient 

        result = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        return result[::-1]