class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # built in method & more efficient
        nums.sort()
        return nums[-k]

        # # Quick Sort Solution
        # def quickSort(nums):
        #     if len(nums) <= 1: return nums

        #     pivot = random.choice(nums)

        #     less_than, equal_to, greater_than = [], [], []

        #     for val in nums:
        #         if val < pivot: less_than.append(val)
        #         elif val > pivot: greater_than.append(val)
        #         else: equal_to.append(val)

        #     return quickSort(less_than) + equal_to + quickSort(greater_than)
        # sortedArr = quickSort(nums)
        # return sortedArr[-k]