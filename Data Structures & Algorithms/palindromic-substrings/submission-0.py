class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAndCount(s,left,right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count = count +1
                left = left - 1
                right = right +1
            return count
        n = len(s)
        totalCount = 0
        for i in range(n):
            #count odd-lenght palindromes (single character center)
            totalCount = totalCount + expandAndCount(s,i,i)
            # count even lenght palindromes (two character center)
            totalCount = totalCount + expandAndCount(s,i,i+1)
        return totalCount

        