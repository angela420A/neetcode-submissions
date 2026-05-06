class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1
        while L <= R:
            M = (L + R) //2
            if matrix[M][-1] < target:
                L = M + 1
            elif matrix[M][0] > target:
                R = M - 1
            else:
                break

        if R < L:
            return False
        
        l, r = 0, len(matrix[0]) -1
        while l <= r:
            m = (l + r) //2
            if matrix[M][m] < target:
                l = m + 1
            elif matrix[M][m] > target:
                r = m - 1
            else:
                return True
        return False