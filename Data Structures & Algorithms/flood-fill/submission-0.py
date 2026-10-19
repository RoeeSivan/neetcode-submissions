class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        if image[sr][sc] == color:
            return image
        orig = image[sr][sc]
        def bfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != orig:
                return
            image[r][c] = color
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)
        bfs(sr,sc)
        return image