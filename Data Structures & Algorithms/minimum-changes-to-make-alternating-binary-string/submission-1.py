class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if int(s[i]) != i % 2:
                count += 1
        return min(count, len(s) - count)