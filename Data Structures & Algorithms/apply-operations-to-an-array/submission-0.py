class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = 0 
        r =  1
        res = [0] * len(nums)
        # first pass
        while r < len(nums):
            if nums[l] == nums[r]:
                nums[r] = 0
                nums[l] = nums[l]*2
            l += 1
            r+= 1
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                res[j] = nums[i]
                j += 1
        return res
