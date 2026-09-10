class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        max_so_far = nums[0]
        min_so_far = nums[0]
        res = nums[0]
        #traverse the array starting from the second element
        for i in range(1,len(nums)):
            current_element = nums[i]
            if current_element < 0:
                max_so_far, min_so_far = min_so_far,max_so_far
            max_so_far = max(current_element, max_so_far * current_element)
            min_so_far = min(current_element, min_so_far * current_element)
            res = max(res,max_so_far)
        return res
