class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        found = False
        counter = Counter(s)
        for c in counter:
            res +=  2 * (counter[c] // 2)
            if counter[c] % 2 == 1:
                found = True
        if found:
            res += 1
        return res