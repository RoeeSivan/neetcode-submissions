class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count_inc = 1
        count_dec = 1
        res = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                count_inc += 1
                count_dec = 1
            if nums[i] > nums[i+1]:
                count_dec += 1
                count_inc = 1
            if nums[i] == nums[i+1]:
                count_dec = 1
                count_inc = 1
            res = max(res,count_dec,count_inc)
        return res


        
