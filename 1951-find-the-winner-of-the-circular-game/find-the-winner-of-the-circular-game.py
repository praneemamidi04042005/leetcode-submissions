class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(1,n+1):
            l.append(i)
        res=0
        while len(l)!=1:
            res=(res+k-1)%len(l)
            l.remove(l[res])
        return l[0]

        