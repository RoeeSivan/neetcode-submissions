class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_dif = float('inf')
        nums.sort()
        for i in range(len(nums) - k +1):
            current_dif = nums[i+ k - 1] - nums[i]
            if current_dif < min_dif:
                min_dif = current_dif
        return min_dif
