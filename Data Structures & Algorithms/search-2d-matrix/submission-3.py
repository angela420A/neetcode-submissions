class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1
        while L <= R:
            M = (L + R) // 2
            if target > matrix[M][-1]:
                L = M + 1
            elif target < matrix[M][0]:
                R = M -1
            else:
                break
        
        l, r = 0, len(matrix[M]) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[M][m]:
                l = m + 1
            elif target < matrix[M][m]:
                r = m - 1
            else:
                return True
        return False