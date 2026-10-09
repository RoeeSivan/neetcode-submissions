class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        n = len(grid)
        flat_copy = [item for row in grid for item in row]
        counter = Counter(flat_copy)
        for c in counter:
            if counter[c] == 2:
                res.append(c)
        for num in range(1,n*n +1):
            if num not in counter:
                res.append(num)
        return res
        