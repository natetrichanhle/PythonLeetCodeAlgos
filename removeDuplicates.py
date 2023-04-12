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

    class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        # both pointers start at index 1 since we know that index 0 is already sorted
        L = 1
        for R in range(1, len(nums)):
            # if the number at the right pointer compared to the number at the index before it is different, then we know it's the first time we've seen it
            if nums[R] != nums[R - 1]:
                # we then want to make the left pointers value equal to the value of right pointer where we discovered the new unique value
                nums[L] = nums[R]
                # after we do all the procedures before this, we increment the left pointer
                L += 1
        # return L which at the end of the iterations, is the amount of unqiue values
        return L
    
    class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            # if nums[i] isn't equal to the value we're trying to find then we want to move those values to the front of the array
            if nums[i] != val:
                nums[k] = nums[i]
                # increment k by 1 every time nums[i] isnt equal to the value 
                k += 1
        # k is the amount of numbers that's left after removing the numbers equal to the value
        return k


        # shorter solution
        # for i in range(nums.count(val)):
        #     nums.remove(val)
        # return len(nums)
