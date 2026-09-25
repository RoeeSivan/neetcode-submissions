class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(k * (k - 1) // 2 for k in counts.values())