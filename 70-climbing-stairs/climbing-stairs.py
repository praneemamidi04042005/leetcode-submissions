class Solution:
    def climbStairs(self, n: int) -> int:
        i,a,b,c=0,0,1,0
        while i<=n:
            c=a+b
            a=b
            b=c
            i+=1
        return a
        