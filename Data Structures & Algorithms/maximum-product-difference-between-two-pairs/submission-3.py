class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        #nlogn sol
        nums = sorted(nums)
        return nums[len(nums)-1] * nums[len(nums)-2] - nums[0] *nums[1]