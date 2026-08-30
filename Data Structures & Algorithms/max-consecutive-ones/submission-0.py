class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        best = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+= 1
                best = max(best,count)
            else:
                count = 0
        return best
        