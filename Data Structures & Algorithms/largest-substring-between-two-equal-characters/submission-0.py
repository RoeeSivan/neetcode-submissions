class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        distances = {}
        res = -1
        for i,char in enumerate(s):
            if char not in distances:
                distances[char] = i
            else:
                res = max(res,i - distances[char] -1)
        return res