class Solution:
    def integerBreak(self, n: int) -> int:
        if n in {2,3}:
            return n-1
        if n%3 == 0:
            return 3**(n//3)
        elif n%3 == 1:
            return (3**(n//3-1))*4
        else:
            return (3**(n//3))*2