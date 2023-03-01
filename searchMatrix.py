class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #  brute force using extra space

        one_dimensional = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                one_dimensional.append(matrix[i][j])
        L = 0
        R = len(one_dimensional) - 1
        while L <= R:
            mid = L + (R - L) // 2
            mid_val = one_dimensional[mid]
            if target > mid_val:
                L = mid + 1
            elif target < mid_val:
                R = mid - 1
            else:
                return True
        return False
