class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        res = 0
        s1 = set()
        for r in range(len(s)):
            while s[r] in s1:
                s1.remove(s[l])
                l += 1
            s1.add(s[r])
            res = max(res,r-l+1)
        return res
