class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable_set, prev_height):
            # Check boundaries, if already visited, or if height is lower than previous
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if (r, c) in reachable_set:
                return
            if heights[r][c] < prev_height:
                return
            
            # Mark current cell as reachable
            reachable_set.add((r, c))

            # Traverse all 4 neighbors (up, down, right, left)
            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])
            
        # Run dfs for pacific borders (top row and left column)
        for c in range(cols):
            dfs(0, c, pacific_reachable, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pacific_reachable, heights[r][0])
            
        # Run dfs for atlantic borders (bottom row and right column)
        for c in range(cols):
            dfs(rows - 1, c, atlantic_reachable, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atlantic_reachable, heights[r][cols - 1])
            
        # Find intersection of the cells reachable by both oceans
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    res.append([r, c])
                    
        return res