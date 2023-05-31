class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3 :
            return n
        cur, prev = 2, 1
        for _ in range(3, n+1):
            prev, cur = cur, cur+prev
        return cur
        
    
   
        
        
    
        