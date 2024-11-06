class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # Edge case: Single element array
        # Edge case: No elements in the array
        if n == 0 or n == 1:
            return 0
        buy = 0
        max_profit = 0
        for sell in range(1, n):
            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell  # slide the window
        return max_profit