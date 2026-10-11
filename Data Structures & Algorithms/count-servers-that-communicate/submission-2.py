class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # מעבר ראשון: סופרים כמה שרתים יש בכל שורה ובכל עמודה.
        # first pass: we count how many servers are there in each row and column
        res = 0 
        m = len(grid)
        n = len(grid[0])
        m_array = [0] * m
        n_array = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    m_array[i] += 1
                    n_array[j] += 1
        for i in range(m):
            for j in range(n):
                if (m_array[i] > 1 or n_array[j] > 1) and (grid[i][j] == 1):
                    res += 1
        return res
