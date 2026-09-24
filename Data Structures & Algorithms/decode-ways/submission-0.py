class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        #dp[i] stores the number of ways to decode the prefix s[0....i-1]
        dp = [0]* (n+1)
        dp[0] = 1 # an empty string has 1 valid empty decoding
        dp[1]= 1 # a single non zero digits has 1 valid decdoing
        for i in range(2,n+1):
            onedigit = s[i-1]
            if onedigit != '0':
                dp[i] = dp[i] +dp[i-1]
            twodigits = int(s[i-2] + s[i-1])
            if twodigits >= 10 and twodigits <= 26:
                dp[i] = dp[i] +dp[i-2]
        return dp[n]