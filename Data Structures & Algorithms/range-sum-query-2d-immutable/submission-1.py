class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])
        self.prefix = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for r in range(ROW):
            total = 0
            for c in range(COL):
                total += matrix[r][c]
                top = self.prefix[r][c + 1]
                self.prefix[r + 1][c + 1] = total + top

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        top = self.prefix[r1 - 1][c2]
        left = self.prefix[r2][c1 - 1]
        upperL = self.prefix[r1 - 1][c1 -1]
        return self.prefix[r2][c2] - top - left + upperL



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)