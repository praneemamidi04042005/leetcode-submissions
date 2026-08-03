class Solution:
    def pivotInteger(self, n: int) -> int:
        s=0
        l=[]
        for i in range(1,n+1):
            l.append(i)
        for i  in range(len(l)):
            s+=l[i]
            if s==sum(l[i:]):
                return i+1
        return -1
        