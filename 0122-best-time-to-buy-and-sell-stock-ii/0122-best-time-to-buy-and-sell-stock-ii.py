class Solution:
    def f(self, idx, stock, prices):
        # Base Case 
        if idx == len(prices):
            return 0
        profit = float('-inf')
        if stock:
            sell = prices[idx] + self.f(idx+1, 0, prices)
            dont_sell = 0 +  self.f(idx+1, 1, prices)
            profit = max(sell, dont_sell)
        else:
            buy = -prices[idx] + self.f(idx+1, 1, prices)
            dont_buy = 0 + self.f(idx+1, 0, prices)
            profit = max(buy, dont_buy)
        return profit 

    def f_memo(self, idx, stock, prices, dp):
        # Base Case 
        if idx == len(prices):
            return 0
        if dp[idx][stock] != -1:
            return dp[idx][stock]
        if stock:
            sell = prices[idx] + dp[idx+1][0]
            dont_sell = 0 +  dp[idx+1][1] 
            dp[idx][stock] = max(sell, dont_sell)
        else:
            buy = -prices[idx] + dp[idx+1][1]
            dont_buy = 0 + dp[idx+1][0]
            dp[idx][stock] = max(buy, dont_buy)

        return dp[idx][stock] 

    def maxProfit_tab(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for i in range(2)] for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        for idx in range(n-1, -1, -1):
            for stock in range(2):
                profit = float('-inf')
                if stock==1:
                    sell = prices[idx] + dp[idx+1][0]
                    dont_sell = 0 +  dp[idx+1][1] 
                    profit = max(sell, dont_sell)
                else:
                    buy = -prices[idx] + dp[idx+1][1]
                    dont_buy = 0 + dp[idx+1][0]
                    profit = max(buy, dont_buy)
                dp[idx][stock] = profit

        return dp[0][0]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cur = [-1 for i in range(2)]
        ahead = [-1 for i in range(2)]
        ahead[0] = ahead[1] = 0
        for idx in range(n-1, -1, -1):
            for stock in range(2):
                profit = float('-inf')
                if stock==1:
                    sell = prices[idx] + ahead[0]
                    dont_sell = 0 +  ahead[1] 
                    profit = max(sell, dont_sell)
                else:
                    buy = -prices[idx] + ahead[1]
                    dont_buy = 0 + ahead[0]
                    profit = max(buy, dont_buy)
                cur[stock] = profit
            ahead = cur
        return ahead[0]
        