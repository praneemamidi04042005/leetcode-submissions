class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        def su(n):
            c=0
            while n>0:
                c+=n%10
                n//=10
            return c
        count=0
        for i in range(low,high+1):
            s=str(i)
            l=len(s)
            m=l//2
            if l%2==1:
                continue
            if su(int(s[:m]))==su(int(s[m:])):
                count+=1
        return count
        