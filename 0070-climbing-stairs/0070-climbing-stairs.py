class Solution:
    #climbStairs(n) - # of ways to reach n th stair from 0
    def climbStairs(self, n: int) -> int:
        if n < 3 : return n
        prev2, prev1= 1, 2
        for i in range(3,n+1):
            prev2, prev1 = prev1, prev2 + prev1 
        return prev1
