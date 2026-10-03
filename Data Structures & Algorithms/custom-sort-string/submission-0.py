class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = ""
        count = Counter(s)
        for char in order:
            if char in count:
                res += char * count[char]
                count[char] = 0
        for i in count:
                res += i * count[i]
        return res
