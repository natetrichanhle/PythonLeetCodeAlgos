class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 1st attempt --> more efficient
        # create a set of unique nums
        # if the length of nums is greater than the length of the unique set then we know that a value appears more than once
        # otherwise return false

        unique = set(nums)
        if len(nums) > len(unique):
            return True
        return False

        # 2nd attempt
        # create a hashset
        # loop through nums
        # if the number is already in the hashset, then we know that there's a dupe
        # otherwise, we add the number 

        # hashset = set()
        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False