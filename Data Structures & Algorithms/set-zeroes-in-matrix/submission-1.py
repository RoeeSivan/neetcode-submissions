class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_array = [False]*(len(matrix)) #number of rows, an array of falses
        col_array = [False]*(len(matrix[0])) #number of columns,an array of falses
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix [i][j] == 0:
                    row_array[i] = True
                    col_array[j] = True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row_array[i] or col_array[j]:
                    matrix[i][j] = 0



        