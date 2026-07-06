class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        l=[]
        i=1
        while n>0:
            if k-i not in l:
                l.append(i)
                n-=1
            i+=1
        return sum(l)
            
        