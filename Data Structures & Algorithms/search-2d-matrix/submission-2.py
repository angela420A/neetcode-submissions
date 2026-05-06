class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])

        top, button = 0, ROW - 1
        while top <= button:
            mid = (top + button) // 2

            if matrix[mid][0] > target:
                button = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        
        l, r = 0, COL - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[mid][m] < target:
                l = m + 1
            elif matrix[mid][m] > target:
                r = m - 1
            else:
                return True
        return False