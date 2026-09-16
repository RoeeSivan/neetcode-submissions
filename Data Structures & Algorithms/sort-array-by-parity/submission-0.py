class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        left = 0
        # we swap each time we find an even number
        # the left pointer keeps the ndext open index that is ready to recieve an even number.
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums    
