class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force
        arr = []
        for i in range(len(nums)):
            res = 1
            for j in range(len(nums)):
                if j!= i:
                    res *= nums[j]
            arr.append(res)
        return arr