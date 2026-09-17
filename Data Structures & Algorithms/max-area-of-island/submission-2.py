class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0 #this is what will be returned
        current_area = 0
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0
        def dfs(r, c):
      # Check bounds and if the current cell is water ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

      # Mark the current land cell as visited by changing '1' to '0'
            grid[r][c] = 0

      # Recursively visit all 4 neighboring directions
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) +1 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = dfs(r, c)
                    if current_area > max_area:
                        max_area = current_area
        return max_area
