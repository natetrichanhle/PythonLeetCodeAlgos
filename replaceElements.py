class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # start at the end
        # keep track of the max value

        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr
