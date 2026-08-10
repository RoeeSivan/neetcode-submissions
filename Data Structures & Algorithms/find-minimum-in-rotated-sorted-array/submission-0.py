class Solution:
    def findMin(self, nums: List[int]) -> int:
        #brute force version
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < curr:
                curr = nums[i]
        return curr
        