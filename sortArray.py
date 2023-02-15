class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # insertion sort -> time limit exceeded because O(n2) time complexity
        
        # we have 2 pointers
        # the i (j + 1) pointer is gonna be the one compared to the j pointer
        # we have to check if i (j + 1) is less than j so we can swap

        # this loops through the array starting at the first index
        for i in range(1, len(nums)):
            # j is set to i-1 for comparisons
            j = i - 1
            # while loop base case is when j >= 0 so we don't go out of bounds
            # while loop nums[j + 1] (basically i) < nums[j] (the neighbor index to the left)
            while j >= 0 and nums[j + 1] < nums[j]:
                # the swap using pythons built in method
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                # iterate to the left to compare other values
                j -= 1
        # return nums after loop is finished executing
        return nums