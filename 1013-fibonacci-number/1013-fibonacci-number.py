class Solution:
    def fib(self, n: int) -> int:
        if n <2:
            return n
        prev, cur= 0, 1
        for i in range(2, n+1):
            prev, cur = cur, prev+cur

        return cur

        