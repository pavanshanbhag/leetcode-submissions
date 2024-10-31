class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # base case includes check on i1,i2<0 thus will use 1 based indexing
        dp = [[0 for _ in range(m+1)] for _ in range(2)] # 2 rows x (m+1) columns
        # initialized to 0
        for i1 in range(1, n+1):
            for i2 in range(1, m+1):
                if text1[i1-1] == text2[i2-1]:
                    dp[i1%2][i2] = 1 + dp[(i1-1)%2][i2-1]
                else :
                    dp[i1%2][i2] = 0 + max(dp[(i1-1)%2][i2], dp[i1%2][i2-1])
        return dp[n%2][-1]
        