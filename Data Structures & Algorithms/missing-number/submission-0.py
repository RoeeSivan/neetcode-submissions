class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        n = len(nums)
        for i in range(n+1):
            found = False
            for j in range(n):
                    if nums[j] == i:
                        found = True
                        break #we found it, thus we stooped looking
            if not found:
                return i
