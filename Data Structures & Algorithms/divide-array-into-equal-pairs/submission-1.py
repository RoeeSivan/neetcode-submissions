class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for num in counter:
            if counter[num] % 2 != 0:
                return False
        return True