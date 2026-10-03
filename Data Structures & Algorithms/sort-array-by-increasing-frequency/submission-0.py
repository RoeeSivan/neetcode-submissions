class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        count = Counter(nums)
        sorted_keys = sorted(count, key=lambda x: (count[x], -x))
        for num in sorted_keys:
            for i in range(count[num]):
                res.append(num)
        return res