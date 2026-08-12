class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(0,32):
            mask = 1 << i # equivalent to doing 2^i
            if mask & n:
                count += 1
        return count