class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
# for each row, we take ith, iith (main diagonal) and ith, jth (antidiagonal) where j decreases from len(mat) - 1 to 0
        res = 0
        j = len(mat) - 1 #number pf rows
        for i in range(len(mat)):
            if i == j:
                res += mat[i][i]
            else:
                res += mat[i][i] + mat[i][j]
            j -= 1
        return res
        