class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0
        #base case substrings of length 1 are always palindromes
        for i in range(0,n):
            dp[i][i] = True
        #base case 2: substring of length2 : 
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2
        #check for lengths greater than 2
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i + k -1 #j is the ending index
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    if k > max_len:
                        start = i
                        max_len = k
                
        return s[start:start + max_len]

        