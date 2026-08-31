class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        up, down = False, False
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                up = True
            if nums[i] > nums[i+1]:
                down = True
        return not(up and down) 
        