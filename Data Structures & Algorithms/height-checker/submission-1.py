class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #by myself
        c = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                c += 1
        return c 