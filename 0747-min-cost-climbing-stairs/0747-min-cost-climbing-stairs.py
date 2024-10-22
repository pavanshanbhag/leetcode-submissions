from collections import defaultdict
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = defaultdict(int)
        n = len(cost)

        # Base Case
        if n < 2:
            return cost[n-1] 
    
        cost.append(0)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2,n+1):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])

        return dp[n]