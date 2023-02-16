class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    #     # insertion sort -> time limit exceeded because O(n2) time complexity
        
    #     # we have 2 pointers
    #     # the i (j + 1) pointer is gonna be the one compared to the j pointer
    #     # we have to check if i (j + 1) is less than j so we can swap

    #     # this loops through the array starting at the first index
    #     for i in range(1, len(nums)):
    #         # j is set to i-1 for comparisons
    #         j = i - 1
    #         # while loop base case is when j >= 0 so we don't go out of bounds
    #         # while loop nums[j + 1] (basically i) < nums[j] (the neighbor index to the left)
    #         while j >= 0 and nums[j + 1] < nums[j]:
    #             # the swap using pythons built in method
    #             nums[j + 1], nums[j] = nums[j], nums[j + 1]
    #             # iterate to the left to compare other values
    #             j -= 1
    #     # return nums after loop is finished executing
    #     return nums

        # merge sort -> 0(nlogn)

        def mergeSort(arr):
            # base case 
            if len(arr) > 1:
                # to get the mid index
                mid = len(arr) // 2
                # to get the left subarray
                L = arr[:mid]
                # to get the right subarray
                R = arr[mid:]
                # recursion for the L and R arrays
                mergeSort(L)
                mergeSort(R)
                # indexes of L (i), R(j), and the arr(k)
                i, j, k = 0, 0, 0
                # merge the two sorted halves into the original array
                while i < len(L) and j < len(R):
                    if L[i] <= R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                # if one of the halves have elements still remaining, we want to just add those values into the sorted array
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
        # recursion for nums
        mergeSort(nums)
        return nums