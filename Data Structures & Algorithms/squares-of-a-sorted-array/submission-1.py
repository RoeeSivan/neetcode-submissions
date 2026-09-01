class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #the largest absolute value will be in the right or left
        res = []
        l = 0
        r = len(nums) - 1
        while l <= r:
            if abs(nums[l]) <= abs(nums[r]):
                res.append(nums[r]**2)
                r -= 1
            elif abs(nums[l]) >= abs(nums[r]):
                res.append(nums[l]**2)
                l += 1
        return res[::-1]