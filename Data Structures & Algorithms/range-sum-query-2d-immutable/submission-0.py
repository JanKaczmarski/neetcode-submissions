class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # matrix len is > 0
        n, m = len(matrix), len(matrix[0])
        # n + 1, m + 1 size for padding
        self.prefix_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            prefix = 0
            for j in range(1, m + 1):
                # offset
                prefix += matrix[i - 1][j - 1]
                self.prefix_sum[i][j] = prefix + self.prefix_sum[i - 1][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefix_sum[r2][c2]
        above = self.prefix_sum[r1 - 1][c2]
        left = self.prefix_sum[r2][c1 - 1]
        topLeft = self.prefix_sum[r1 - 1][c1 - 1]

        return bottomRight - above - left + topLeft


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)