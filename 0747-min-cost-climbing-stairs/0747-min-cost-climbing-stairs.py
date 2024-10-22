from collections import defaultdict
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = defaultdict(int)
        n = len(cost)
        cost.append(0)
        
        dp[n] = 0
        dp[0] = cost[0]
        if n <= 1:
            return cost[0] 
        dp[1] = min(cost[1], dp[0]+cost[1]) 

        for i in range(2,n+1):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])

        return dp[n]