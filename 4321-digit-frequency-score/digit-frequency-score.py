class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        hm={}
        while n>0:
            hm[n%10]=hm.get(n%10,0)+1
            n//=10
        s=0
        for i in hm:
            s+=i*hm[i]
        return s
        