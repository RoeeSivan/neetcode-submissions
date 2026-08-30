class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []    
        triangle = [[1]]
        for i in range(1, numRows):
            prev_row = triangle[-1]
        # Start the row with 1, add the sums of adjacent elements, and end with 1
            new_row = [1] + [prev_row[j] + prev_row[j+1] for j in range(len(prev_row) - 1)] + [1]
            triangle.append(new_row)
        return triangle
