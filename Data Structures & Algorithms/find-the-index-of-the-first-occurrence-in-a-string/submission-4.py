class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s,f = 0,0
        n = 0
        while n <= len(needle) -1 and s <= len(haystack) -1 and f <= len(haystack) -1:
            if haystack[f] == needle[n]:
                f += 1
                n += 1
                if n == len(needle):
                    return s
            else: #mismatch
                s += 1
                f = s
                n = 0
        return -1


        