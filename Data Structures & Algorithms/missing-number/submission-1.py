class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result1 = 0
        result2 = 0
        for i in range(n+1):
            result1 ^= i
        for j in nums:
            result2 ^= j
        return result1 ^ result2
        

        