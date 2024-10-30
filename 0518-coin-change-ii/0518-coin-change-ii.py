class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n, target = len(coins), amount
        dp = [[0 for _ in range(target+1)] for _ in range(n)] # target*n
        # Base Case
        for i in range(len(coins)):
            dp[i][0] = 1
        for i in range(len(coins)):
            for j in range(1, target + 1):
                take = 0
                if coins[i] <= j:
                    take = dp[i][j - coins[i]]
                not_take = dp[i - 1][j] if i > 0 else 0
                dp[i][j] = take + not_take
        return dp[-1][-1] # dp[n-1][target] # dp[-1][-1]
                 