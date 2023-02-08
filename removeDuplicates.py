class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # since it's sorted we know that duplicates are next to each other
        # two pointers - one that traverses until it is a diff number and one that stays for the comparison
        
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
        return left       