class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf') for _ in range(amount+1)] for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][0] = 0
        for t in range(1,amount+1):
            dp[0][t] = t // coins[0] if t % coins[0] == 0 else float("inf")

        # fill dp array
        for i in range(1, n):
            for t in range(1, amount+1):
                nottake = 0 + dp[i-1][t]
                take = float('inf')
                if coins[i] <= t:
                    take = 1 + dp[i][t-coins[i]]
                dp[i][t] = min(take, nottake)
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
        