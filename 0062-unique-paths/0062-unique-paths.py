class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # base case
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        
        for row in range(1, m):
            for col in range (1, n):
                up, left = 0, 0
                # boundary case
                if row-1 > -1:
                    up = dp[row-1][col]
                if col-1 > -1: 
                    left = dp[row][col-1]
                
                dp[row][col] = up + left 
        return dp[m-1][n-1]