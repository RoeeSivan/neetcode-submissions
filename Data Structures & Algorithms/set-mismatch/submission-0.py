class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        res = []
        counter = Counter(nums)
        for num in counter:
            if counter[num] == 2:
                res.append(num)
        for num in range(1,len(nums) + 1):
            if num not in nums_set:
                res.append(num)
        return res