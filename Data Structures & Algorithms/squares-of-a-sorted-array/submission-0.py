class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            num = i *i
            res.append(num)
        return sorted(res)
