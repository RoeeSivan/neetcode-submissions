class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        counter = Counter(arr)
        for num in counter:
            if counter[num] == num:
                res = max(res,num)
        return res