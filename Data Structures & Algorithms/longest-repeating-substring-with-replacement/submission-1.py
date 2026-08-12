class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        n = len(s)
        seen = defaultdict(int)
        for r in range(n):
            seen[s[r]] += 1
            while (r - l+ 1) - max(seen.values()) > k:
                seen[s[l]] -= 1
                l+= 1
            res = max(res,r-l +1)
        return res

