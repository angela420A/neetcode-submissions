class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, but = 0, ROWS-1

        while top <= but:
            md = (top + but) //2
            if target > matrix[md][COLS-1]:
                top = md + 1
            elif target < matrix[md][0]:
                but = md - 1
            else:
                break

        if top > but:
            return False
        
        l, r = 0, COLS-1
        while l <= r:
            m = (l + r) //2
            if target < matrix[md][m]:
                r = m - 1
            elif target > matrix[md][m]:
                l = m + 1
            else:
                return True
        return False