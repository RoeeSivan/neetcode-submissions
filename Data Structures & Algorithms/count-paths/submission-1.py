class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    #initialize a single row of size n with all 1, there is only 1 way to reach any cell in the first row 
        row = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                row[j] += row[j-1]
        return row[-1]

        
        