class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
    # 'i' is the slow pointer tracking unique elements
        i = 0 
    # 'j' is the fast pointer exploring the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


        