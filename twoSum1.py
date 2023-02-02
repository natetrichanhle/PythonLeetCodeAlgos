class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a hashmap to keep track of the previous values and indexes that didn't satisfy our current condition
        # loop through the nums 
        # instatiate a difference variable of target - num (number we are currently at)
        # if the difference is already in the hashmap we return the index of that value and the current index
        # then we continue and add the number & its index into the hashmap
        hashmap = {} # value:index
        for index, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[num] = index
        return