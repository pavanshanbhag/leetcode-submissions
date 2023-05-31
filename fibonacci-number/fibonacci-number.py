class Solution:
    def fib(self, n: int) -> int:
        prev, cur = 0, 1
        if n < 2:
            return n
        for _ in range(2, n+1):
            prev, cur = cur, prev+cur
        return cur
        
        
        
        