class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force
        for row in matrix:
            for element in row:
                if element == target:
                    return True
        return False


        