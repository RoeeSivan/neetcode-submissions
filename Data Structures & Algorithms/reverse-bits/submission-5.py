class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #smarter solution
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res
        