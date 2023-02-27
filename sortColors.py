class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort method

        # list to hold the quantity of how many times a val has popped up in nums
        counts = [0, 0, 0]
        
        # add the quantity of each val in nums
        for n in nums:
            counts[n] += 1

        # fill each bucket in the original array
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1
        return nums
