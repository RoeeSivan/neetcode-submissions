class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        # initialize queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        minutes = 0
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        # BFS traversal level by level
        while queue and fresh_count > 0:
            size = len(queue)
            rotted_in_this_minute = False
            for i in range(size):
                curr_r, curr_c = queue.popleft()
                for dr, dc in directions:
                    neighbor_r = curr_r + dr
                    neighbor_c = curr_c + dc
                    # check bounds first, then if the neighbor is a fresh orange
                    if 0 <= neighbor_r < rows and 0 <= neighbor_c < cols and grid[neighbor_r][neighbor_c] == 1:
                        grid[neighbor_r][neighbor_c] = 2
                        fresh_count -= 1
                        queue.append((neighbor_r, neighbor_c))
                        rotted_in_this_minute = True
            if rotted_in_this_minute:
                minutes += 1
        if fresh_count == 0:
            return minutes
        else:
            return -1