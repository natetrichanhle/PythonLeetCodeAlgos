class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # #  FIRST SOLUTION ALLOCATING EXTRA SPACE

        # # use extra space to make the matrix a 1D list
        # one_dimensional = []
        # for i in range(len(matrix)):
        #      for j in range(len(matrix[i])):
        #          one_dimensional.append(matrix[i][j])
        # # binary search
        # L = 0
        # R = len(one_dimensional) - 1
        # while L <= R:
        #     mid = L + (R - L) // 2
        #     mid_val = one_dimensional[mid]
        #     if target > mid_val:
        #         L = mid + 1
        #     elif target < mid_val:
        #         R = mid - 1
        #     else:
        #         return True
        # return False

        # DOUBLE BINARY SEARCH METHOD

        # 1st binary search portion of the algo
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            # the midpoint of the rows
            mid_row = top + (bot - top) // 2
            # compared to the right most value of the row
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            # compared to the left most value of the row
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break
        # if none of the rows contained the target value
        if not (top <= bot):
            return False

        # 2nd binary search portion of the algo

        # the row that we found with the target value
        mid_row = top + (bot - top) // 2
        L, R = 0, COLS - 1
        while L <= R:
            mid = L + (R - L) // 2
            mid_val = matrix[mid_row][mid]
            if target > mid_val:
                L = mid + 1
            elif target < mid_val:
                R = mid - 1
            else:
                return True
        return False
