class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev_s = s[::-1] # reverse of s
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # Base case is i1<0 or i2<0 results in 0, shifting index to keep index positive
        # base case already taken care as 0 is used to initialize dp array
        for i1 in range(1, n+1):
            for i2 in range(1, n+1):
                if s[i1-1] == rev_s[i2-1] : # 0 based indexing 
                    dp[i1][i2] = 1 + dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = 0 + max(dp[i1-1][i2],dp[i1][i2-1])
                    
        return dp[-1][-1] # dp[n][n]